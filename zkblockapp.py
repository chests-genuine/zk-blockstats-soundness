# app.py
import os
import sys
import json
import time
import argparse
from datetime import datetime
from web3 import Web3

DEFAULT_RPC = os.environ.get("RPC_URL", "https://mainnet.infura.io/v3/YOUR_INFURA_KEY")


def get_block_info(w3: Web3, block_number: int) -> dict:
    """
    Retrieve block details and compute key statistics.
    """
    try:
        block = w3.eth.get_block(block_number)
        gas_used = block.gasUsed
        gas_limit = block.gasLimit
        gas_ratio = gas_used / gas_limit if gas_limit else 0
        tx_count = len(block.transactions)
        return {
            "number": block.number,
            "timestamp": block.timestamp,
            "gas_used": gas_used,
            "gas_limit": gas_limit,
            "gas_utilization": round(gas_ratio * 100, 2),
            "tx_count": tx_count,
            "miner": block.miner,
            "hash": block.hash.hex(),
        }
    except Exception as e:
        raise RuntimeError(f"Error fetching block info: {e}")


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="zk-blockstats-soundness — analyze EVM block stats, gas usage, and miner activity for zk rollup and Web3 soundness validation."
    )
    p.add_argument("--rpc", default=DEFAULT_RPC, help="EVM RPC URL (default from RPC_URL)")
    p.add_argument("--block", type=int, help="Block number to analyze (required)", required=True)
    p.add_argument("--json", action="store_true", help="Output results as JSON")
    p.add_argument("--timeout", type=int, default=30, help="RPC timeout (default 30 seconds)")
    return p.parse_args()


def main() -> None:
    start = time.time()
    args = parse_args()

    if not args.rpc.startswith("http"):
        print("❌ Invalid RPC URL format. It must start with 'http' or 'https'.")
        sys.exit(1)

    w3 = Web3(Web3.HTTPProvider(args.rpc, request_kwargs={"timeout": args.timeout}))
    if not w3.is_connected():
        print("❌ RPC connection failed. Check RPC_URL or --rpc argument.")
        sys.exit(1)

    print(f"🕒 Timestamp: {datetime.utcnow().isoformat()}Z")
    print("🔧 zk-blockstats-soundness")
    print(f"🔗 RPC: {args.rpc}")
    print(f"🧱 Block: {args.block}")

    try:
        data = get_block_info(w3, args.block)
    except Exception as e:
        print(f"❌ {e}")
        sys.exit(2)

    utc_time = datetime.utcfromtimestamp(data["timestamp"]).isoformat() + "Z"

    print(f"🧭 Block Number: {data['number']}")
    print(f"⏰ Timestamp (UTC): {utc_time}")
    print(f"🪙 Miner: {data['miner']}")
    print(f"⛽ Gas Used: {data['gas_used']} / {data['gas_limit']} ({data['gas_utilization']}%)")
    print(f"📊 Transactions: {data['tx_count']}")
    print(f"🔹 Block Hash: {data['hash']}")

    # ✅ New: Add simple classification for gas efficiency
    if data["gas_utilization"] > 90:
        print("🔥 High Gas Utilization: The block is almost full.")
    elif data["gas_utilization"] < 30:
        print("💤 Low Gas Utilization: Sparse transaction activity.")
    else:
        print("⚖️ Normal Gas Utilization: Balanced block usage.")

    elapsed = round(time.time() - start, 2)
    print(f"⏱️ Completed in {elapsed:.2f}s")

    if args.json:
        data.update(
            {
                "rpc": args.rpc,
                "timestamp_utc": datetime.utcnow().isoformat() + "Z",
                "elapsed_seconds": elapsed,
            }
        )
        print(json.dumps(data, ensure_ascii=False, indent=2))

    sys.exit(0)


if __name__ == "__main__":
    main()
