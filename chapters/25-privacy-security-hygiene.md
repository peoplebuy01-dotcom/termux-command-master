# Chapter 25 — Privacy और Security Hygiene

- Termux को trusted source से update रखें।
- अनजान scripts को `curl | bash` से सीधे execute न करें।
- GitHub पर API keys, passwords और private keys न डालें।
- Android permissions केवल जरूरत के अनुसार दें।
- Public Wi-Fi पर sensitive accounts के लिए HTTPS और account MFA उपयोग करें।
- Backup में भी निजी data सुरक्षित रखें।

## Secret scan habit
Commit से पहले `git diff --cached` देखकर सुनिश्चित करें कि कोई token/password stage नहीं हुआ। गलती से secret publish हो जाए तो उसे revoke/rotate करें; केवल file delete करना पर्याप्त नहीं।
