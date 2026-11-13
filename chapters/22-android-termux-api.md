# Chapter 22 — Android और Termux:API

Termux:API Android सुविधाओं को Termux scripts से उपयोग करने का optional bridge है। इसके लिए compatible Termux:API add-on app और package की जरूरत हो सकती है; दोनों trusted official source और matching release channel से लें।

## Setup overview
1. Termux और Termux:API add-on compatible source से install करें।
2. Termux में `pkg install termux-api` चलाएँ।
3. Android permission prompts पढ़कर ही अनुमति दें।
4. उपलब्ध commands देखने के लिए `termux-` prefix की सहायता लें।

फोन के contacts, messages, location या microphone जैसे sensitive data को बिना स्पष्ट जरूरत और अनुमति access न करें।
