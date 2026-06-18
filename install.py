#!/usr/bin/env python3
"""
Installeur SYLOX
Auteur : devyl404
"""

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

RESET = "\033[0m"
BOLD = "\033[1m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"

ROOT = Path(__file__).resolve().parent
DEPENDENCIES_DIR = ROOT / "dependencies"
ZPHISHER_REPO_URL = "https://github.com/htr-tech/zphisher.git"
CAMPHISH_REPO_URL = "https://github.com/LakshyaSharma207/CamPhish.git"
ANGRYOXIDE_REPO_URL = "https://github.com/Ragnt/AngryOxide.git"
FLUXION_REPO_URL = "https://github.com/FluxionNetwork/fluxion.git"
CUPP_REPO_URL = "https://github.com/Mebus/cupp.git"


def print_status(message, color=CYAN):
    print(f"{color}{message}{RESET}")


def ensure_dependencies_dir():
    if not DEPENDENCIES_DIR.exists():
        DEPENDENCIES_DIR.mkdir(parents=True, exist_ok=True)
        print_status(f"[+] dossier créé : {DEPENDENCIES_DIR}", GREEN)


def ensure_system_tools():
    print_status("\n[+] vérification des outils système...", CYAN)

    for tool in ["bash", "curl"]:
        if shutil.which(tool):
            print_status(f"[✓] {tool} déjà présent", GREEN)
        else:
            print_status(f"[!] {tool} manquant, installation en cours...", YELLOW)

            if os.geteuid() == 0:
                run_command(["apt-get", "update"], check=False)
                run_command(["apt-get", "install", "-y", tool], check=False)
            else:
                run_command(["sudo", "apt-get", "update"], check=False)
                run_command(["sudo", "apt-get", "install", "-y", tool], check=False)

    print_status(
        "[+] installation des paquets requis : php openssh-server wget qrencode bc cowpatty isc-dhcp-server hostapd lighttpd mdk4 php-cgi xterm",
        YELLOW
    )

    if os.geteuid() == 0:
        run_command([
            "apt-get", "install", "-y",
            "php",
            "openssh-server",
            "wget",
            "qrencode",
            "bc",
            "cowpatty",
            "isc-dhcp-server",
            "hostapd",
            "lighttpd",
            "mdk4",
            "php-cgi",
            "xterm",
            "rustup"
        ], check=False)
    else:
        run_command([
            "sudo", "apt-get", "install", "-y",
            "php",
            "openssh-server",
            "wget",
            "qrencode",
            "bc",
            "cowpatty",
            "isc-dhcp-server",
            "hostapd",
            "lighttpd",
            "mdk4",
            "php-cgi",
            "xterm",
            "rustup"
        ], check=False)

    if shutil.which("qrencode"):
        print_status("[✓] qrencode est maintenant disponible", GREEN)
    else:
        print_status(
            "[!] qrencode est introuvable après l'installation. Tentative de correction...",
            YELLOW
        )

        if os.geteuid() == 0:
            run_command(["apt-get", "install", "-y", "qrencode"], check=False)
        else:
            run_command(["sudo", "apt-get", "install", "-y", "qrencode"], check=False)


def run_command(command, check=True, env=None, timeout=1000):
    try:
        cmd_env = os.environ.copy()
        if env:
            cmd_env.update(env)
        result = subprocess.run(
            command,
            cwd=ROOT,
            text=True,
            capture_output=True,
            stdin=subprocess.DEVNULL,
            check=check,
            env=cmd_env,
            timeout=timeout,
        )
        output = (result.stdout or "") + (result.stderr or "")
        if output:
            print(output.strip())
        return result.returncode
    except subprocess.CalledProcessError as e:
        output = (e.stdout or "") + (e.stderr or "")
        if output:
            print(output)
        if check:
            print_status("[!] échec de la commande", RED)
            return e.returncode
        print_status("[!] installation non réalisée ou bloquée par les droits sudo", YELLOW)
        return e.returncode
    except subprocess.TimeoutExpired:
        print_status("[!] le clone GitHub a pris trop de temps. Vérifie ta connexion ou la disponibilité du dépôt.", RED)
        return 124


def parse_args():
    parser = argparse.ArgumentParser(description="Installateur SYLOX")
    parser.add_argument("--skip-launch", action="store_true", help="ne pas lancer tool.py à la fin")
    return parser.parse_args()


def install_repo(launch_tool=True):
    ensure_dependencies_dir()
    ensure_system_tools()
    print_status("\n[SYLOX] Installation des dépendances...", PURPLE)

    zphisher_path = DEPENDENCIES_DIR / "zphisher"
    if zphisher_path.exists():
        print_status(f"[i] le dépôt zphisher existe déjà : {zphisher_path}", YELLOW)
        print_status("[i] mise à jour via git pull...", CYAN)
        run_command(["git", "-C", str(zphisher_path), "pull", "--ff-only"], env={"GIT_TERMINAL_PROMPT": "0"})
    else:
        print_status(f"[+] clonage depuis {ZPHISHER_REPO_URL}", GREEN)
        result = run_command(["git", "clone", "--depth", "1", ZPHISHER_REPO_URL, str(zphisher_path)], check=False, env={"GIT_TERMINAL_PROMPT": "0"})
        if result != 0:
            print_status("[!] le clonage zphisher a échoué. Le dépôt peut être inaccessible ou nécessiter un accès GitHub spécifique.", RED)
        else:
            print_status(f"[✓] zphisher installé dans {zphisher_path}", GREEN)

    camphish_path = DEPENDENCIES_DIR / "CamPhish"
    if camphish_path.exists():
        print_status(f"[i] le dépôt CamPhish existe déjà : {camphish_path}", YELLOW)
        print_status("[i] mise à jour via git pull...", CYAN)
        run_command(["git", "-C", str(camphish_path), "pull", "--ff-only"], env={"GIT_TERMINAL_PROMPT": "0"})
    else:
        print_status(f"[+] clonage depuis {CAMPHISH_REPO_URL}", GREEN)
        result = run_command(["git", "clone", "--depth", "1", CAMPHISH_REPO_URL, str(camphish_path)], check=False, env={"GIT_TERMINAL_PROMPT": "0"})
        if result != 0:
            print_status("[!] le clonage CamPhish a échoué. Le dépôt peut être inaccessible ou nécessiter un accès GitHub spécifique.", RED)
        else:
            print_status(f"[✓] CamPhish installé dans {camphish_path}", GREEN)

    angryoxide_path = DEPENDENCIES_DIR / "AngryOxide"
    if angryoxide_path.exists():
        print_status(f"[i] le dépôt AngryOxide existe déjà : {angryoxide_path}", YELLOW)
        print_status("[i] mise à jour via git pull...", CYAN)
        run_command(["git", "-C", str(angryoxide_path), "pull", "--ff-only"], env={"GIT_TERMINAL_PROMPT": "0"})
    else:
        print_status(f"[+] clonage depuis {ANGRYOXIDE_REPO_URL}", GREEN)
        result = run_command(["git", "clone", "--depth", "1", ANGRYOXIDE_REPO_URL, str(angryoxide_path)], check=False, env={"GIT_TERMINAL_PROMPT": "0"})
        if result != 0:
            print_status("[!] le clonage AngryOxide a échoué. Le dépôt peut être inaccessible ou nécessiter un accès GitHub spécifique.", RED)
        else:
            print_status(f"[✓] AngryOxide installé dans {angryoxide_path}", GREEN)

    fluxion_path = DEPENDENCIES_DIR / "fluxion"
    if fluxion_path.exists():
        print_status(f"[i] le dépôt Fluxion existe déjà : {fluxion_path}", YELLOW)
        print_status("[i] mise à jour via git pull...", CYAN)
        run_command(["git", "-C", str(fluxion_path), "pull", "--ff-only"], env={"GIT_TERMINAL_PROMPT": "0"})
    else:
        print_status(f"[+] clonage depuis {FLUXION_REPO_URL}", GREEN)
        result = run_command(["git", "clone", "--depth", "1", FLUXION_REPO_URL, str(fluxion_path)], check=False, env={"GIT_TERMINAL_PROMPT": "0"})
        if result != 0:
            print_status("[!] le clonage Fluxion a échoué. Le dépôt peut être inaccessible ou nécessiter un accès GitHub spécifique.", RED)
        else:
            print_status(f"[✓] Fluxion installé dans {fluxion_path}", GREEN)

    

    cupp_path = DEPENDENCIES_DIR / "cupp"
    if cupp_path.exists():
        print_status(f"[i] le dépôt cupp existe déjà : {cupp_path}", YELLOW)
        print_status("[i] mise à jour via git pull...", CYAN)
        run_command(["git", "-C", str(cupp_path), "pull", "--ff-only"], env={"GIT_TERMINAL_PROMPT": "0"})
    else:
        print_status(f"[+] clonage depuis {CUPP_REPO_URL}", GREEN)
        result = run_command(["git", "clone", "--depth", "1", CUPP_REPO_URL, str(cupp_path)], check=False, env={"GIT_TERMINAL_PROMPT": "0"})
        if result != 0:
            print_status("[!] le clonage cupp a échoué. Le dépôt peut être inaccessible ou nécessiter un accès GitHub spécifique.", RED)
        else:
            print_status(f"[✓] cupp installé dans {cupp_path}", GREEN)

    if launch_tool:
        print_status("\n[+] lancement de tool.py...", GREEN)
        os.execv(sys.executable, [sys.executable, str(ROOT / "tool.py")])
    else:
        print_status("\n[✓] installation terminée. Relance tool.py quand tu veux.", GREEN)


def main():
    args = parse_args()
    print(f"{BOLD}{PURPLE}")
    print("   ███████╗██╗   ██╗██╗      ██████╗ ██╗  ██╗")
    print("   ██╔════╝╚██╗ ██╔╝██║     ██╔═══██╗╚██╗██╔╝")
    print("   ███████╗ ╚████╔╝ ██║     ██║   ██║ ╚███╔╝")
    print("   ╚════██║  ╚██╔╝  ██║     ██║   ██║ ██╔██╗")
    print("   ███████║   ██║   ███████╗╚██████╔╝██╔╝ ██╗")
    print("   ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝")
    print(f"{RESET}")
    print_status("[SYLOX] Installateur de dépendances", PURPLE)
    install_repo(launch_tool=not args.skip_launch)


if __name__ == "__main__":
    main()
