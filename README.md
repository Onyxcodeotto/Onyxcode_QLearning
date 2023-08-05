# Percobaan QLearning dalam Pathfinding

Repositori ini adalah percobaan implementasi QLearning pada game dengan peraturan berikut:
1. Terdapat papan 1 dimensi (gerakan kiri kanan saja) sepanjang 10 kotak
2. Terdapat lubang di titik 0, dan apel di titik 9
3. Player berada pada titik 2 dan dapat bergerak ke kiri atau kanan
4. Jika player jatuh ke dalam lubang, point yang didapatkan -100, jika player mendapatkan apel, point yang didapatkan +100. Jika player menempati titik lain, player akan mendapatkan point -1
5. ika player jatuh ke lubang atau mendapatkan apel, player kembali ke titik 3
6. Player menang saat mendapatkan point +500
7. Player kalah saat mendapatkan point -200

## Cara menjalankan
Pada command line di root repositori ini, jalankan command "python main.py"
Dari ini, program akan membuat qtable serta path untuk memenangkan game ini.