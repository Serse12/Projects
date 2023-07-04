import random

def generadomanda(argomenti):
     x = random.randint(0, len(argomenti)-1)

     y = random.randint(0, len(argomenti[x][1])-1)

     print("Parlami del " + argomenti[x][0] + " più precisamente del " + argomenti[x][1][y])



def fillcapitolo2(capitolotemp):
    capitolo=capitolotemp[1]
    capitolo[0]="Domini, perimetro e superficie di attacco"
    capitolo[1]="Architettura di base"
    capitolo[2]="Router, Firewall e Sonde"
    capitolo[3]="Osservare il Traffico: Sniffing"
    capitolo[4]="Necessità di strumenti di monitoraggio"
    capitolo[5]="Network monitoring"

def fillcapitolo3(capitolotemp):
    capitolo=capitolotemp[1]
    capitolo[0]="Firewall"
    capitolo[1]="Firewall: azioni possibili"
    capitolo[2]="Firewall: modalità operative"
    capitolo[3]="Filtraggio sul bordo (border router e firewall)"
    capitolo[4]="Parametri di filtraggio"
    capitolo[5]="Filtraggio stateless e statefull"
    capitolo[6]="Session Filtering"
    capitolo[7]="Politiche di filtraggio e Content filtering"
    capitolo[8]="Controllo Accessi a livello utente"
    capitolo[9]="Le Architetture AAA"
    capitolo[10]="RADIUS"
    capitolo[11]="Il Modello di Access Control (modello astratto e implementazioni)"
    capitolo[12]="ACL vs Capability Lists"
    capitolo[13]="Meccanismi di filtraggio del traffico: ACL"
    capitolo[14]="Spoofing dell’indirizzo IP"
    capitolo[15]="Traffico consentito in uscita e in ingresso"
    capitolo[16]="Strategie per il Controllo Accessi"
    capitolo[17]="Gestione ridondanza"
    capitolo[18]="Architetture per il controllo degli accessi"
    capitolo[19]="Network Access Control (NAC) e componenti"


def fillcapitolo4(capitolotemp):
    capitolo=capitolotemp[1]
    capitolo[0]="Evoluzione del perimetro"
    capitolo[1]="Limiti di un firewall"
    capitolo[2]="Nuove necessità: Agile Security"
    capitolo[3]="Il problema: Siloed Security"
    capitolo[4]="Orchestrazione e Condivisione"
    capitolo[5]="Automazione e Threat Intelligence"
    capitolo[6]="UTM(unified threat management) e Next Generation Firewalls"
    capitolo[7]="Next Generation Firewalls Funzionalità Fondamentali"
    capitolo[8]="Advanced (Deep) packet inspection"
    capitolo[9]="Classificazione del traffico"
    capitolo[10]="Blocco di applicazioni che offuscano traffico"
    capitolo[11]="Intrusion Detection e Prevention"
    capitolo[12]="Differenze fra IDS e Firewalls"
    capitolo[13]="Intrusion Prevention"
    capitolo[14]="Componenti Architetturali IDS/IPS"
    capitolo[15]="Operatività IDS/IPS Approcci e implementazioni"
    capitolo[16]="Problemi IDS/IPS"
    capitolo[17]="Approcci Misuse detection"
    capitolo[18]="Signature"
    capitolo[19]="Limitazioni delle Signatures Statiche"
    capitolo[20]="Approcci Anomaly-based"
    capitolo[21]="Sandboxes"
    capitolo[22]="Sistemi di Log Management e SIEM"
   
def fillcapitolo5(capitolotemp):
    capitolo=capitolotemp[1]
    capitolo[0]="Modelli di attacco: la triade CIA"
    capitolo[1]="Attacchi Passivi e Attacchi Attivi"
    capitolo[2]="Attacchi Passivi: Sniffing"
    capitolo[3]="Scansione: Network mapping"
    capitolo[4]="Portscan"
    capitolo[5]="Tool di scansione: NMAP"
    capitolo[6]="Contromisure al port scanning: PSAD"
    capitolo[7]="Attacchi (D)DoS"
    capitolo[8]="Botnets come vettori di attacco"
    capitolo[9]="ICMP Flooding"
    capitolo[10]="Attacchi DDoS: Reflection"
    capitolo[11]="DDoS: Broadcast Amplification"
    capitolo[12]="Attacchi DDoS: DNS Amplification"
    capitolo[13]="Attacchi DDoS: NTP Amplification"
    capitolo[14]="Attacchi DDoS: Memcache Amplification"
    capitolo[15]="Resource Starvation Attacks"
    capitolo[16]="Slowloris"
    capitolo[17]="Rudy (R-U-Dead-Yet?)"
    capitolo[18]="LOIC"
    capitolo[19]="SSL/TLS Handshake attack"
    capitolo[20]="Landing"
    capitolo[21]="Ping of Death"
    capitolo[22]="Teardrop"
    capitolo[23]="TCP SYN Flooding e Low rate TCP SYN Flood"
    capitolo[24]="SYN flood con backscattering"
    capitolo[25]="Soluzioni al SYN flood"
    capitolo[26]="Flood non bloccabili: TCP con flood"
    capitolo[27]="Hijacking"
    capitolo[28]="Il ruolo dei DNS"
    capitolo[29]="BIND: cache poisoning e spoofing"
    capitolo[30]="DNSSEC"
    capitolo[31]="Iniezione di routes inesistenti (RIP)"
    capitolo[32]="Attacchi BGP"
    capitolo[33]="Cracking Sessioni cifrate (BGP)"
    capitolo[34]="Meccanismi S-BGP"
    capitolo[35]="MPLS"

def fillcapitolo6(capitolotemp):
    capitolo=capitolotemp[1]
    capitolo[0]="Worm"
    capitolo[1]="Automatizzare la reazione"
    capitolo[2]="Morris Worm"
    capitolo[3]="Code Red"
    capitolo[4]="Blaster Worm"
    capitolo[5]="Slammer Worm"
    capitolo[6]="Il caso di Conficker"
    capitolo[7]="Stuxnet"
    capitolo[8]="Worms: Strategie di infezione"
    capitolo[9]="Modelli di diffusione"
    capitolo[10]="Considerazioni strategiche"
    capitolo[11]="Botnets"
    capitolo[12]="Meccanismi di propagazione"
    capitolo[13]="Comandi eseguibili da un bot"
    capitolo[14]="Fast-Flux"
    capitolo[15]="Waledac"
    capitolo[16]="Zeus Botnet"
    capitolo[17]="Mirai IoT bot"
    capitolo[18]="Botnet Detection"
    capitolo[19]="Contromisure"
    capitolo[20]="Rilevamento di Honeypot"
    capitolo[21]="Rilevamento Network-Based"
    capitolo[22]="Rilevamento Host-Based"
    capitolo[23]="Rilevamento Anomaly Based"

def fillcapitolo7(capitolotemp):
    capitolo=capitolotemp[1]
    capitolo[0]="Definizioni"
    capitolo[1]="Evidenze digitali in rete"
    capitolo[2]="Cookies"
    capitolo[3]="E-Tag"
    capitolo[4]="Comunicazioni sicure: Cifratura di flusso"
    capitolo[5]="Proxy anonimizzatori"
    capitolo[6]="Mix Network"
    capitolo[7]="Onion routing"
    capitolo[8]="The Onion Router (TOR)"
    capitolo[9]="Attacchi a Tor"
    capitolo[10]="Pubblicazione anonima"
    capitolo[11]="Email Anonime"
    capitolo[12]="VPN: concetti generali"

def fillcapitolo8(capitolotemp):
    capitolo=capitolotemp[1]
    capitolo[0]="Mail Spoofing"
    capitolo[1]="E-Mail Spamming"
    capitolo[2]="MUA o MTA?"
    capitolo[3]="Open Relay"
    capitolo[4]="Come gestire lo spam"
    capitolo[5]="Black&white-listing, RBL"
    capitolo[6]="Filtri di contenuti"
    capitolo[7]="Sender Policy Framework"
    capitolo[8]="DKIM"
    capitolo[9]="Graylisting"
    capitolo[10]="User training"
    capitolo[11]="Vouch by Reference"
    capitolo[12]="Spam Assassin"

def fillcapitolo9(capitolotemp):
    capitolo=capitolotemp[1]
    capitolo[0]="Protezione transazioni: SSL/TLS"
    capitolo[1]="SSL/TLS in HTTP: HTTPS"
    capitolo[2]="Attacchi Man in the middle"
    capitolo[3]="Vulnerablità lato sito"
    capitolo[4]="Code injection attacks"
    capitolo[5]="Instruction-Set Randomization"
    capitolo[6]="SQL Injection Attacks:"
    capitolo[7]="Cross-Site-Scripting (XSS)"
    capitolo[8]="JavaScript"
    capitolo[9]="Furto cookie sessione"
    capitolo[10]="XSS persistente"
    capitolo[11]="Attributi di sessione"

def fillcapitolo10(capitolotemp):
    capitolo=capitolotemp[1]
    capitolo[0]="Tracciamento a ritroso"
    capitolo[1]="Tipi di Analisi"
    capitolo[2]="Complessità analisi"
    capitolo[3]="Analisi: Importanza Timeline"
    capitolo[4]="Whois Query Syntax"
    capitolo[5]="La catena di cooperazione:CSIRT"
    capitolo[6]="Security Advisory"



def main():
    argomenti = dict()

    argomenti[0]=("Capitolo 2: Monitoraggio e NetworkAnalisys",dict())
    fillcapitolo2(argomenti[0])

    argomenti[1]=("Capitolo 3: Politiche di sicurezza e Controllo Accessi",dict())
    fillcapitolo3(argomenti[1])

    argomenti[2]=("Capitolo 4: Next Generation Firewalls e Intrusion Detection Systems",dict())
    fillcapitolo4(argomenti[2])

    argomenti[3]=("Capitolo 5: Attacchi in rete",dict())
    fillcapitolo5(argomenti[3])

    argomenti[4]=("Capitolo 6: Internet Worms",dict())
    fillcapitolo6(argomenti[4])

    argomenti[5]=("Capitolo 7: Anonimato in Rete",dict())
    fillcapitolo7(argomenti[5])

    argomenti[6]=("Capitolo 8: E-Mail Security",dict())
    fillcapitolo8(argomenti[6])

    argomenti[7]=("Capitolo 9: Web Security",dict())
    fillcapitolo9(argomenti[7])

    argomenti[8]=("Capitolo 10: Network Tracing & Incident Response",dict())
    fillcapitolo10(argomenti[8])

    generadomanda(argomenti)



if __name__=="__main__":
    while True:
        input()
        main()


