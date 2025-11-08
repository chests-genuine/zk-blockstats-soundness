# zk-blockstats-soundness

## Overview
**zk-blockstats-soundness** is a CLI utility that analyzes Ethereum and EVM-compatible block data.  
It helps measure **gas utilization**, **miner performance**, and **transaction density** for zk-rollups like **Aztec**, **Zama**, or any general Web3 network.  
This tool is ideal for monitoring **block soundness**, ensuring blocks are fully utilized and consistent across nodes.

## Features
- 🧱 Fetch full block metadata (hash, miner, timestamp, gas usage, transaction count)  
- ⛽ Compute gas utilization percentage  
- ⚙️ Detect high or low gas efficiency patterns  
- 📊 Provide real-time network activity insights  
- 🌍 Works across all EVM-compatible RPCs  
- 💾 JSON output for monitoring and dashboards  

## Installation
1. Requires Python 3.9+  
2. Install dependencies:
   pip install web3
3. Set your RPC endpoint:
   export RPC_URL=https://mainnet.infura.io/v3/YOUR_KEY

## Usage
Analyze a block:
   python app.py --block 21000000

Use a custom RPC:
   python app.py --rpc https://arb1.arbitrum.io/rpc --block 21000000

Output as JSON:
   python app.py --block 21000000 --json

## Example Output
🕒 Timestamp: 2025-11-08T14:45:19.312Z  
🔧 zk-blockstats-soundness  
🔗 RPC: https://mainnet.infura.io/v3/YOUR_KEY  
🧱 Block: 21000000  
🧭 Block Number: 21000000  
⏰ Timestamp (UTC): 2023-10-25T08:31:16Z  
🪙 Miner: 0x829BD824B016326A401d083B33D092293333A830  
⛽ Gas Used: 29500000 / 30000000 (98.33%)  
📊 Transactions: 182  
🔹 Block Hash: 0x54b3eab993e2cd51999fbd8c761a1c8a2bafcfae9c8e942e4b98301b9f6a5555  
🔥 High Gas Utilization: The block is almost full.  
⏱️ Completed in 0.48s  

## Notes
- **Gas Utilization Metric:** Indicates how efficiently block space is being used.  
- **Block Soundness:** Ensures blocks are processed consistently across different nodes.  
- **ZK Applications:** Useful for tracking block density relevant to proof generation or rollup compression.  
- **Performance Insight:** Identify blocks that are under-utilized or congested.  
- **Multi-Network Support:** Works with Ethereum, Polygon, Base, Arbitrum, Optimism, and private devnets.  
- **Security Tip:** Always use a trusted RPC endpoint for audit operations.  
- **Data Accuracy:** Block timestamps are reported in UTC for consistent time-based analysis across nodes.  
- **Automation Ready:** JSON output integrates with Prometheus, Datadog, or custom CI systems for live monitoring.  
- **Cross-Layer Analysis:** You can compare L1 and L2 block utilization to understand rollup efficiency.  
- **Future Extensions:** Planned additions include tracking base fees, blob gas metrics (EIP-4844), and validator participation rates.  
- **Exit Codes:**  
  - `0` → Success  
  - `2` → RPC or block fetch error.  
