# Similarity, Syntax & Unit Testing for Automated Code Grading
> 

# Introduction

<h4>Motivation</h4> 
<p>Our team originally planned to implement an AI model for automatically scanning the license plate when the vehicle want to park</p>

<h4>Present slides: <a href=https://www.canva.com/design/DAFjhbSZAdY/gYEx7tmvrlS9z0Pk7vO0PA/view?utm_content=DAFjhbSZAdY&utm_campaign=designshare&utm_medium=link&utm_source=homepage_design_menu>here</a></h4>

<h4>Report submission: <a href=https://github.com/GHxKw/IoT_Project-main/blob/main/IOT_PROJECT_REPORT.pdf>here<a/></h4>

<h2 id="table-of-contents"> :book: Table of Contents</h2>
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#general-information">General Information</a></li>
    <li><a href="#features">Features</a></li>
    <li>
      <a href="#setup">Setup</a>
       <ul>
        <li><a href="https://github.com/GHxKw/IoT_Project-main/tree/main/arduino">Arduino</a></li>
        <li><a href="https://github.com/GHxKw/IoT_Project-main/tree/main/mobile">Mobile</a></li>
        <li><a href="https://github.com/GHxKw/IoT_Project-main/tree/main/client">Client</a></li>
        <li><a href="https://github.com/GHxKw/IoT_Project-main/tree/main/server">Server</a></li>
       </ul>
    </li>
    <li><a href="#technologies">Technologies</a></li>
    <li><a href="#folder-structure">Folder Structure</a></li>
    <li><a href="#screenshot">Screenshot</a></li>
    <li><a href="#acknowledgement">Acknowledgement</a></li>
  </ol>
</details>

<h2 id="general-information"> 🧮 General Information</h2>

- **Arduino** : For uploading code to make the automatically executing from the Arduino UNO R3
- **Mobile** : Using Flutter to build the UI of mobile application
- **Client** : Using Vitejs is a tool to build ReactJS UI
- **Server** : Using FLask framework to build the server

<h2 id="features"> 📋 Features</h2>

List the ready features here:

| ----- | Features | 
| ----- | ----- |
| Arduino | Checking distance, automatically open the barrier when having the signal, LED on to guide customer to the parking slot |
| Mobile | Login, Register, Homepage, Profile, Logout |
| Client | View user active, Take license plate picture |
| Server | Authentication, OCR scanning, Facial recognition |

<h2 id="setup"> 🧰 Setup</h2>
  <ul>
    <li><a href="https://github.com/GHxKw/IoT_Project-main/tree/main/arduino">Arduino</a></li>
    <li><a href="https://github.com/GHxKw/IoT_Project-main/tree/main/mobile">Mobile</a></li>
    <li><a href="https://github.com/GHxKw/IoT_Project-main/tree/main/client">Client</a></li>
    <li><a href="https://github.com/GHxKw/IoT_Project-main/tree/main/server">Server</a></li>
   </ul>
 
<h2 id="technologies"> 🖥️ Technologies</h2>

### 1. Mobile
| Plugin | README |
| ------ | ------ |
| Flutter | https://github.com/flutter/flutter |

### 2. Client
| Plugin | README |
| ------ | ------ |
| Vite | https://github.com/vitejs/vite |

### 3. Server
| Plugin | README |
| ------ | ------ |
| Flask | https://github.com/pallets/flask |

<!-- FOLDER STRUCTURE -->
<h2 id="folder-structure"> 🗺️ Folder Structure</h2>
    
    ├── Compress_the_string
    │   ├── Corret
    │   │── ref.py
    │   │── Test_program
    │   │   ├── app.py
    │   │   ├── winnowing.py
    │   │   ├── generate_ast.py
    │   │   ├── conftest.py
    │   │   ├── test_script.py
    │   │   ├── unit_test_program.py
   
    ├── client
    │   ├── src
    │   │   ├── actions
    │   │   ├── components
    │   │   ├── styles
    │   │   ├── Container.jsx
    │   │   ├── global.css
    │   │   ├── main.jsx
   
    ├── server
    │   ├── src
    │   │   ├── controllers
    │   │   ├── data
    │   │   ├── database
    │   │   ├── routes
    │   │   ├── app.js
  
<h2 id="diagram"> 🖥 Diagrams </h2>

<h3> Process diagram </h3> 
<img src="https://res.cloudinary.com/nguyenle23/image/upload/v1685077153/iot/iSP_yraak5.png" alt="process_diagram" />

<h2 id="screenshot"> 📸 Screenshots </h2>

### Mobile
<img src="https://res.cloudinary.com/nguyenle23/image/upload/v1685077343/iot/mobile_uyyor0.png" alt="mobile_img" />

### Client
<img src="https://res.cloudinary.com/nguyenle23/image/upload/v1685077406/iot/web_hro3i8.png" alt="web_img" />

<h2 id="acknowledgement"> 💼 Acknowledgement </h2>

### What We Learnt
- Communicating and connecting between hardware and software
- Implementation of AI technology with IoT system
- Usage of different frameworks and libaries
- Usage of Git, pull, merge and commit
- Organize files to better manage development
- Importance of README.md
