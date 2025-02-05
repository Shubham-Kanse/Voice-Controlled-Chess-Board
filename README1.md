# 🎙️ Voice-Controlled Chess Board

![Inspiration Image](resources/harrypotterchessinspiration.jpeg)

## **📌 Introduction**
The **Voice-Controlled Chess Board** is an innovative system designed to allow users to play chess without physical interaction. Using **voice commands**, players can move pieces on a real chessboard, making it **accessible for individuals with physical disabilities** or anyone looking for a **hands-free chess experience**.

This project integrates **speech recognition, an X-Y axis motorized movement system, and an electromagnetic piece-handling mechanism** to create an **intuitive and engaging gameplay experience**.

---

## **🎯 Features**
✅ **Voice-activated chess movements** using a Bluetooth-connected smartphone  
✅ **Real-time piece tracking** and position updates  
✅ **Electromagnetic mechanism** to lift and move pieces  
✅ **X-Y axis stepper motor system** for precise piece movement  
✅ **Hands-free gaming experience** for accessibility  
✅ **Fair play detection** by distinguishing different players' voices  

---

## **🔬 How It Works**

### 🎙️ **Voice Command Processing**
- Players use an **Android app ("Arduino Voice Control")** to speak commands like:  
  ```
  "Move A2 to A4"
  ```
- The app converts speech to text and transmits it via **Bluetooth (HC-05 module)** to a **Raspberry Pi (Rpi)**.

### 📡 **Command Interpretation**
- The Rpi **processes the move** and checks if it follows **chess rules**.
- If the move is **valid**, it triggers the **piece movement system**.

### ⚙️ **Piece Movement Mechanism**
- A **stepper motor-driven X-Y axis mechanism** moves the piece.
- An **electromagnet (or solenoid)** lifts and places the piece in the correct position.
- If an opponent’s piece is present, it is **removed and placed in a storage box**.

### 📟 **Game Updates & Display**
- The system **updates the board's position data** and signals the **next move using an LED indicator**.
- The cycle **repeats for each player’s turn**.

---

## **🛠️ Project Components**

### 🖥️ **Hardware**
- **Raspberry Pi 4** (Main processing unit)
- **HC-05 Bluetooth Module** (Communication between mobile and board)
- **NEMA 17 Stepper Motors** (For X-Y axis movement)
- **Electromagnet / Solenoid** (For picking up chess pieces)
- **Plastic Chess Pieces with Metal Base**
- **16x2 LCD Display** (For move validation and feedback)
- **Power Supply & Motor Drivers**

📜 [View Full Hardware Components List and Specifications link](docs/hardware_components.md)


### 🛠️ **Software & Libraries**
- **Python** (For processing voice commands and controlling hardware)
- **Google Speech API** (For voice-to-text conversion)
- **Stockfish (optional)** (For AI-based opponent play)
- **Arduino IDE** (For interfacing Bluetooth communication)

---

## **🔧 Setup & Installation**

### 📲 **1. Install Required Software**
```sh
sudo apt update && sudo apt upgrade
sudo apt install python3 python3-pip
pip install pyserial speechrecognition
```
- Install **Arduino Voice Control App** on your Android device.

### 🔌 **2. Connect Hardware**
- Set up **Raspberry Pi** with the **HC-05 Bluetooth module**.
- Connect **stepper motors and electromagnet** using appropriate motor drivers.
- Ensure the **chess pieces have a metallic base** for magnetic interaction.

### 🎙️ **3. Run the Chess Board System**
```sh
python3 src/voice_chess.py
```
- Speak commands like **"Move A2 to A4"** into the Android app.
- The **board will automatically move the piece** to the desired position.

---

## **🔍 Challenges & Improvements**

### ✅ **Completed**
- **Successfully implemented voice control** and **real-time chess piece movement**.
- **Improved stability** by replacing wheels with **electric wire guards** for smooth movement.
- **Replaced the electromagnet** with a **solenoid** for better grip on pieces.
- **Used a Bluetooth module instead of a microphone** for more accurate speech recognition.

### 🚀 **Future Enhancements**
- **Multiplayer Online Mode** – Connect with players worldwide via the internet.
- **AI Opponent Integration** – Use **Stockfish Chess Engine** for playing against AI.
- **Improved Voice Accuracy** – Fine-tune speech recognition for better response.
- **Compact & Portable Design** – Make the system **lighter and travel-friendly**.

---

## **🙌 Contributors**
👤 **Shubham Kanse**  
👤 **Omkar Kamble**  
👤 **Sakshi Lohiya**

---
