This is a repository where main methods discussed in the Blockchain-related courses given by Dr. Baniata, Hamza and Dr. Kertesz, Attila at the University of Szeged are implemented.

- "IB0125E: Introduction to Blockchain Technology (BSc level)"
- "IMN0100E: Blockchain Fundamentals and Applications (PhD and MSc levels)"

Main Bitcoin methods implemented in this code:
- 
- Full node and light node simulation
- Asymmetric encryption (exemplified by RSA cryptography)
- Bitcoin block generalized structure
- Block verification and chaining
- Proof-of-Work (PoW) mining
- Simplified Payment Verification (SPV) using Merkle Tree/Root
- Simulated TX with extensible UTXO TX model

Future additions:
-
- Implementing the full UTXO model, including its verification
- Implementing ECC instead of RSA
- Utilization of Bitcoin addresses
- Demonstrating the BFT of PoW while solving BGP using the networkx library to demonstrate the network.
- etc.

Steps to run the code (on linux):
-
- To install python 3.8: https://www.python.org/downloads/
- To install apt: https://manpages.debian.org/buster/apt/apt.8.en.html Or sudo apt update
- To install pip3: sudo apt install python3-pip
- Make sure you have git: "sudo apt install git"
- clone the repository: "git clone https://github.com/HamzaBaniata/BlockchainCourse.git"
- install any missing libraries: "for instance: To install rsa: sudo apt install python3-rsa"
- Type python3 blockchain.py in the command line.
