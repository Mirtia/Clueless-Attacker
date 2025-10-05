#!/usr/bin/env python3
"""
BDS LKM Rootkit Client Simulator
Simulates client-side actions for connecting to a BDS rootkit
"""

import sys
import os
import argparse

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from clueless_attacker.attack import BDSRootkitClient

def main():
    print(r"""
   _____ _            _                         _   _             _
  / ____| |          | |                   /\  | | | |           | |
 | |    | |_   _  ___| | ___  ___ ___     /  \ | |_| |_ __ _  ___| | _____ _ __
 | |    | | | | |/ _ \ |/ _ \/ __/ __|   / /\ \| __| __/ _` |/ __| |/ / _ \ '__|
 | |____| | |_| |  __/ |  __/\__ \__ \  / ____ \ |_| || (_| | (__|   <  __/ |
  \_____|_|\__,_|\___|_|\___||___/___/ /_/    \_\__|\__\__,_|\___|_|\_\___|_|
    """)
    parser = argparse.ArgumentParser(description="Imitates an attacker's post infection actions after loading an LKM.")
    parser.add_argument("--target", "-t", default="192.168.0.102",
                       help="Target IP address (default: 192.168.0.102)")
    parser.add_argument("--attack", "-a",
                       choices=["reverse", "bind", "escalation", "all"],
                       help="Attack type to simulate")

    args = parser.parse_args()

    client = BDSRootkitClient(args.target)

    if args.attack == "reverse":
        client.simulate_reverse_shell_attack()
    elif args.attack == "bind":
        client.simulate_bind_shell_attack()
    elif args.attack == "escalation":
        client.simulate_privilege_escalation()
    elif args.attack == "all":
        print("Running all attack simulations...")
        client.simulate_reverse_shell_attack()
        client.simulate_bind_shell_attack()
        client.simulate_privilege_escalation()
    else:
        # Show available options if no attack specified
        print("BDS LKM Rootkit Client Simulator")
        print("Available attack options:")
        print("  --attack reverse        Reverse shell attack")
        print("  --attack bind           Bind shell attack")
        print("  --attack escalation     Privilege escalation")
        print("  --attack all            Run all simulations")
        print()
        print("Example: python bin/main.py --attack reverse --target 192.168.1.100")

if __name__ == "__main__":
    main()
