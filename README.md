# Mikoshi--Your-Secure-Vault
Safeguarding Your Data, Empowering Your Crypto Wallet

# Development of a UPI-like Protocol for BTC Wallets

## Overview

Cryptocurrency, particularly Bitcoin, is often viewed with apprehension due to the absence of a legal framework and regulation. The anonymity of Bitcoin transactions makes it challenging for traditional law enforcement to trace a user's identity. Our system seeks to address these concerns by collecting certain personal data in exchange for a safer and more convenient method of conducting blockchain transactions.

### Objectives
- **Ease of Use**: Simplifying Bitcoin transactions to make them as accessible as UPI payments.
- **Fraud Prevention**: Ensuring secure transactions and reducing scams or misuse.
- **Identity Linking**: Associating Bitcoin wallets with government-issued identification for enhanced accountability.
- **Encouraging Adoption**: Enabling everyday users to adopt cryptocurrencies in their daily transactions.

---

## Technology Stack

### Frontend
- **Languages**: HTML, CSS, JavaScript
- **Library**: HTMX (for seamless front-end to back-end communication)

### Backend
- **Framework**: Flask (Python-based lightweight web server)
- **Blockchain API**: Bitcoin Core SDK

### Database
- **Database**: MongoDB (for robust and scalable data storage)

---

## System Features

### 1. **Wallet Validation System**
   - Links a user's Bitcoin wallet with their Aadhar card and PAN card details.
   - Stores personal information securely in a MongoDB database.

### 2. **Identity Integration**
   - Gives identities to wallets and Bitcoin addresses by linking them with governmental data.
   - Allows regulatory authorities to trace illegal activities back to the source.

### 3. **Custom Wallet and QR Code**
   - Generates a custom wallet linked to the user's identity.
   - Provides a QR code that represents the user's public key for seamless transactions.

### 4. **Mainstream Adoption**
   - Promotes the use of Bitcoin for everyday transactions.
   - Aims to reduce the fear of fraud and increase cryptocurrency adoption among the general public.

---

## Workflow

1. **User Registration**:
   - User inputs their Aadhar card, PAN card, and basic personal details.
   - The system validates and links these details with the user's Bitcoin wallet.

2. **Wallet Creation**:
   - Generates a custom Bitcoin wallet and associates it with the validated identity.
   - QR code is generated for easy transactions.

3. **Transaction Execution**:
   - Users can conduct Bitcoin transactions using the QR code and wallet, similar to UPI systems.
   - Backend ensures secure and validated interactions with the Bitcoin blockchain.

4. **Regulatory Oversight**:
   - Authorized entities can trace any fraudulent or illegal activities via the linked identities.

---

## Installation and Usage

### Prerequisites
- Python 3.9+
- MongoDB
- Bitcoin Core

### Steps to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/btc-upi-protocol.git
   cd btc-upi-protocol

