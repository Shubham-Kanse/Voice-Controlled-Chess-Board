# 📋 Hardware Components List

| **Component**                           | **Quantity** | **Function** |
|-----------------------------------------|-------------|-------------|
| **Raspberry Pi (Rpi)**                  | 1           | Main processing unit for receiving and processing commands |
| **HC-05 Bluetooth Module**              | 1           | Enables wireless communication between mobile app and Raspberry Pi |
| **NEMA 17 Stepper Motors**              | 2           | Controls movement along X and Y axes |
| **A4988 Stepper Motor Drivers**         | 2           | Controls stepper motor operation |
| **Electromagnet / Solenoid**            | 1           | Picks up and drops chess pieces |
| **16x2 LCD Display (Optional)**         | 1           | Displays move validation and feedback |
| **Power Supply (12V, 5V)**              | 1           | Provides power to motors and Raspberry Pi |
| **Acrylic Chessboard with Metal Grid**  | 1           | Custom board for proper movement of pieces |
| **Plastic Chess Pieces with Metal Base**| 32          | Enables electromagnet to lift pieces |
| **Wires, Connectors, and Breadboard**   | -           | Required for circuit connections |

---

## 📖 **Component Documentation & Datasheets**

### 🖥️ **Raspberry Pi (Rpi)**
- **Official Documentation:** [Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/)
- **Specifications:** [Raspberry Pi 4 Model B Specs](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/specifications/)

### 🔵 **HC-05 Bluetooth Module**
- **Datasheet:** [HC-05 Datasheet (PDF)](https://components101.com/sites/default/files/component_datasheet/HC-05%20Datasheet.pdf)
- **Pinout and Guide:** [HC-05 Module Pinout](https://components101.com/wireless/hc-05-bluetooth-module)

### ⚙️ **NEMA 17 Stepper Motors**
- **Datasheet:** [NEMA 17 Stepper Motor](https://www.omc-stepperonline.com/download/17HS19-2004S1.pdf)

### 🛠 **A4988 Stepper Motor Driver**
- **Product Info:** [A4988 Stepper Motor Driver](https://www.pololu.com/product/1182)

### 🧲 **Electromagnet / Solenoid**
- **Product Guide:** [Electromagnet - 12VDC](https://www.adafruit.com/product/387)

### 📟 **16x2 LCD Display (Optional)**
- **Guide:** [16x2 LCD with I2C](https://www.arduino.cc/en/Tutorial/HelloWorld)

### 🔋 **Power Supply**
- **Raspberry Pi Power Guide:** [Official Pi Power Supply](https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#power-requirements)

---

## ⚡ **Wiring & Setup**
Ensure proper wiring of:
- **HC-05 Bluetooth module** to **Raspberry Pi UART (TX/RX)**
- **NEMA 17 stepper motors** to **A4988 drivers** via GPIO
- **Electromagnet** controlled via **relay switch**
- **LCD Display (if used)** connected via **I2C**

---

📌 **Maintained by:** Shubham Kanse  
📅 **Last Updated:** `2020/10/01`
