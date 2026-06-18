#!/usr/bin/env python3
"""
SYLOX - faux outil de style "hack" CLI
Auteur : devyl404
Thème : violet / cyberpunk / terminal
"""

import os
import shlex
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
PURPLE = "\033[95m"
CYAN = "\033[96m"
BLUE = "\033[94m"
MAGENTA = "\033[35m"
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_header():
    banner = f"""
{BOLD}{MAGENTA}
   ███████╗██╗   ██╗██╗      ██████╗ ██╗  ██╗
   ██╔════╝╚██╗ ██╔╝██║     ██╔═══██╗╚██╗██╔╝
   ███████╗ ╚████╔╝ ██║     ██║   ██║ ╚███╔╝
   ╚════██║  ╚██╔╝  ██║     ██║   ██║ ██╔██╗
   ███████║   ██║   ███████╗╚██████╔╝██╔╝ ██╗
   ╚══════╝   ╚═╝   ╚══════╝ ╚═════╝ ╚═╝  ╚═╝
{RESET}
{BOLD}{PURPLE}                 by Devyl404{RESET}
"""
    print(banner)


def print_menu():
    print(f"\n{BOLD}{PURPLE}Menu principal{RESET}")
    print(f"{CYAN}1.{RESET} {YELLOW}zphisher{RESET}")
    print(f"{CYAN}2.{RESET} {YELLOW}camphish{RESET}")
    print(f"{CYAN}3.{RESET} {YELLOW}wifi{RESET}")
    print(f"{CYAN}5.{RESET} {YELLOW}cupp{RESET}")
    print(f"{CYAN}99.{RESET} {YELLOW}retour à install.py{RESET}")
    print()
    print(f"{DIM}Choisis une option : {RESET}", end="")


def fake_loading(label, steps=6):
    print(f"\n{PURPLE}[{label}]{RESET} initialisation...", end="", flush=True)
    for i in range(steps):
        time.sleep(0.25)
        print("■", end="", flush=True)
    print(f" {GREEN}ok{RESET}\n")


def run_tool(tool_name):
    clear_screen()
    print_header()
    print(f"\n{BOLD}{MAGENTA}Mode sélectionné : {tool_name}{RESET}\n")

    if tool_name == "wifi":
        print(f"{YELLOW}Choix Wi-Fi :{RESET}")
        print(f"{CYAN}1.{RESET} {YELLOW}AngryOxide{RESET}")
        print(f"{CYAN}2.{RESET} {YELLOW}Fluxion{RESET}")
        print()
        choice = input(f"{DIM}Choisis une option Wi-Fi : {RESET}").strip()

        if choice == "1":
            repo_dir = Path(__file__).resolve().parent / "dependencies" / "AngryOxide"
            if not repo_dir.exists():
                print(f"{RED}[!] Le dépôt AngryOxide n'a pas encore été installé.{RESET}")
                print(f"{YELLOW}Exécute d'abord install.py.{RESET}\n")
                input("Appuie sur Entrée pour revenir au menu...")
                return
            print(f"{BLUE}[>] Déplacement dans : {repo_dir}{RESET}")
            print(f"{CYAN}[>] Exécution : sudo bash install.sh{RESET}\n")
            try:
                if os.geteuid() == 0:
                    subprocess.run(["bash", "install.sh"], cwd=repo_dir, check=True)
                else:
                    subprocess.run(["sudo", "bash", "install.sh"], cwd=repo_dir, check=True)

                print(f"{GREEN}[✓] Installation AngryOxide terminée.{RESET}")
                for candidate in [Path("/usr/local/bin/angryoxide"), Path("/usr/bin/angryoxide"), repo_dir / "angryoxide"]:
                    if candidate.exists():
                        print(f"{CYAN}[>] Lancement : {candidate}{RESET}")
                        subprocess.run([str(candidate)], check=False)
                        break
                else:
                    print(f"{YELLOW}[i] Aucun binaire de lancement trouvé automatiquement.{RESET}")
            except subprocess.CalledProcessError as e:
                print(f"{RED}[!] La commande a échoué avec le code {e.returncode}.{RESET}")
                print(f"{YELLOW}[!] Vérifie que sudo est disponible et que tu as les droits root.{RESET}")
            except FileNotFoundError:
                print(f"{RED}[!] bash introuvable sur le système.{RESET}")
        elif choice == "2":
            repo_dir = Path(__file__).resolve().parent / "dependencies" / "fluxion"
            if not repo_dir.exists():
                print(f"{RED}[!] Le dépôt Fluxion n'a pas encore été installé.{RESET}")
                print(f"{YELLOW}Exécute d'abord install.py.{RESET}\n")
                input("Appuie sur Entrée pour revenir au menu...")
                return
            print(f"{BLUE}[>] Déplacement dans : {repo_dir}{RESET}")
            print(f"{CYAN}[>] Exécution : sudo bash fluxion.sh{RESET}\n")
            try:
                if os.geteuid() == 0:
                    subprocess.run(["bash", "fluxion.sh"], cwd=repo_dir, check=True)
                else:
                    subprocess.run(["sudo", "bash", "fluxion.sh"], cwd=repo_dir, check=True)

                print(f"{GREEN}[✓] Installation Fluxion terminée.{RESET}")
                for candidate in [Path("/usr/local/bin/fluxion"), Path("/usr/bin/fluxion"), repo_dir / "fluxion"]:
                    if candidate.exists():
                        print(f"{CYAN}[>] Lancement : {candidate}{RESET}")
                        subprocess.run([str(candidate)], check=False)
                        break
                else:
                    print(f"{YELLOW}[i] Aucun binaire de lancement trouvé automatiquement.{RESET}")
            except subprocess.CalledProcessError as e:
                print(f"{RED}[!] La commande a échoué avec le code {e.returncode}.{RESET}")
                print(f"{YELLOW}[!] Vérifie que sudo est disponible et que tu as les droits root.{RESET}")
            except FileNotFoundError:
                print(f"{RED}[!] bash introuvable sur le système.{RESET}")
        else:
            print(f"{RED}[!] Choix Wi-Fi invalide.{RESET}")

        print(f"\n{PURPLE}Appuie sur Entrée pour revenir au menu...{RESET}", end="")
        input()
        return

    if tool_name == "zphisher":
        repo_dir = Path(__file__).resolve().parent / "dependencies" / "zphisher"
        if not repo_dir.exists():
            print(f"{RED}[!] Le dépôt zphisher n'a pas encore été installé.{RESET}")
            print(f"{YELLOW}Exécute d'abord install.py.{RESET}\n")
            input("Appuie sur Entrée pour revenir au menu...")
            return

        print(f"{BLUE}[>] Déplacement dans : {repo_dir}{RESET}")
        print(f"{CYAN}[>] Exécution : bash zphisher.sh{RESET}\n")
        try:
            subprocess.run(["bash", "zphisher.sh"], cwd=repo_dir, check=True)
        except subprocess.CalledProcessError as e:
            print(f"{RED}[!] La commande a échoué avec le code {e.returncode}.{RESET}")
        except FileNotFoundError:
            print(f"{RED}[!] bash introuvable sur le système.{RESET}")

        print(f"\n{PURPLE}Appuie sur Entrée pour revenir au menu...{RESET}", end="")
        input()
        return

    if tool_name == "camphish":
        repo_dir = Path(__file__).resolve().parent / "dependencies" / "CamPhish"
        if not repo_dir.exists():
            print(f"{RED}[!] Le dépôt CamPhish n'a pas encore été installé.{RESET}")
            print(f"{YELLOW}Exécute d'abord install.py.{RESET}\n")
            input("Appuie sur Entrée pour revenir au menu...")
            return

        print(f"{BLUE}[>] Déplacement dans : {repo_dir}{RESET}")
        print(f"{CYAN}[>] Exécution : bash camphish.sh{RESET}\n")
        try:
            subprocess.run(["bash", "camphish.sh"], cwd=repo_dir, check=True)
        except subprocess.CalledProcessError as e:
            print(f"{RED}[!] La commande a échoué avec le code {e.returncode}.{RESET}")
        except FileNotFoundError:
            print(f"{RED}[!] bash introuvable sur le système.{RESET}")

        print(f"\n{PURPLE}Appuie sur Entrée pour revenir au menu...{RESET}", end="")
        input()
        return

    

    if tool_name == "cupp":
        repo_dir = Path(__file__).resolve().parent / "dependencies" / "cupp"
        if not repo_dir.exists():
            print(f"{RED}[!] Le dépôt cupp n'a pas encore été installé.{RESET}")
            print(f"{YELLOW}Exécute d'abord install.py.{RESET}\n")
            input("Appuie sur Entrée pour revenir au menu...")
            return

        print(f"{BLUE}[>] Déplacement dans : {repo_dir}{RESET}")
        print(f"{CYAN}[>] Exécution : python3 cupp.py -h puis ouverture d'un shell interactif{RESET}\n")
        try:
            command = f"cd {shlex.quote(str(repo_dir))} && python3 cupp.py -h; exec bash"
            os.execvpe("bash", ["bash", "--noprofile", "--norc", "-i", "-c", command], os.environ)
        except FileNotFoundError:
            print(f"{RED}[!] bash introuvable sur le système.{RESET}")

        return

    print(f"{PURPLE}Appuie sur Entrée pour revenir au menu...{RESET}", end="")
    input()


def main():
    while True:
        clear_screen()
        print_header()
        print_menu()
        choice = input().strip()

        if choice == "1":
            run_tool("zphisher")
        elif choice == "2":
            run_tool("camphish")
        elif choice == "3":
            run_tool("wifi")
        elif choice == "5":
            run_tool("cupp")
        elif choice == "99":
            print(f"\n{PURPLE}[>] Lancement de install.py...{RESET}")
            os.execv(sys.executable, [sys.executable, str(ROOT / "install.py"), "--skip-launch"])
        elif choice in {"q", "quit", "exit"}:
            print(f"\n{PURPLE}Fin de la session SYLOX.{RESET}")
            sys.exit(0)
        else:
            print(f"\n{RED}Option inconnue.{RESET}")
            time.sleep(0.7)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{RED}Interruption reçue. Fermeture de SYLOX.{RESET}")
        sys.exit(0)