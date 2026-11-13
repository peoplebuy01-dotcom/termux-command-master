# Chapter 14 — Local Web Server

## Python server
केवल अपनी test files के लिए:
```bash
mkdir -p ~/web-demo
cd ~/web-demo
echo "Hello from my phone" > index.html
python -m http.server 8000 --bind 127.0.0.1
```
अपने ही फोन के browser में `http://127.0.0.1:8000` खोलें। Server रोकने के लिए terminal में Ctrl+C।

## जरूरी सुरक्षा
यह basic development server है, production server नहीं। इसे public internet पर expose न करें। किसी दूसरे device से access देने से पहले firewall, authentication और network exposure की समझ जरूरी है।

## Common errors
- Address already in use: दूसरा port चुनें।
- Page नहीं खुलता: server चल रहा है या नहीं और URL/port जाँचें।

## अभ्यास
एक HTML file बनाकर local browser में देखें।
