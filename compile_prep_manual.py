"""Legacy public manual compiler disabled to prevent disclosure of private source data."""
import sys
sys.stdout.reconfigure(encoding="utf-8")
if __name__ == "__main__":
    sys.exit("Use build_private_vault.py with the local private source files. Public manual compilation is disabled.")
