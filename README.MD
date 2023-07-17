The code for Part1 is present in basic folder.
To run part1 follow :
1. Open VM's terminal, go to 
```
cd “/home/p4/tutorials/exercises/basic”
```
2. Run 
```
make clean
```
3. Run 
```
make run
```

4. You are now on the mininet prompt.Run below commands to open the Host terminals:
```
xterm h1
xterm h2
```
5. Commands to run on h2’s terminal 
```
bash h2-arp.sh 
python server.py 
```
6. Command to run on  h1’s terminal 
```
bash h1-arp.sh 
python client.py 
```


The code for Part2 is present in star folder.
To run part 2:

1. Open VM's terminal, go to 
```
cd "/home/p4/tutorials/exercises/star"
```
2. Run 
```
make clean
```
3. Run 
```
make run
```

4. You are now on the mininet prompt.Run below commands to open the Host terminals:
```
xterm h1
xterm h2
xterm h3
```
5. Commands to run on h3’s terminal 
```
bash h3-arp.sh 
python server.py 
```
6. Commands to run on h2’s terminal 
```
bash h2-arp.sh 
python cache.py 
```
7. Command to run on  h1’s terminal 
```
bash h1-arp.sh 
python client.py 
```



