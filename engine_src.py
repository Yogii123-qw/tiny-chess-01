import os,json,urllib.request as u
V=[0,100,320,330,500,900,0]
W8=[0,0,1,1,2,4,0]
KN=[-33,-31,-18,-14,14,18,31,33]
KD=[-17,-16,-15,-1,1,15,16,17]
BD=[-17,-15,15,17]
RD=[-16,-1,1,16]
CM=[15]*128
for s,b in ((4,12),(0,13),(7,14),(116,3),(112,7),(119,11)): CM[s]=b
def mk(t,v,d):
 a=[0]*128
 for r in range(8):
  for f in range(8):
   x=(ord(t[((7-r) if d else r)*4+min(f,7-f)])-107)*5+v
   a[r*16+f]=x if d else -x
 return a
SM=[0]*13; SE=[0]*13
for k,(a,b,mv,ev) in enumerate((('kkkkuuuummoqllmpkkkoljiklmmgkkkk','kkkkuuuummoqllmpkkkoljiklmmgkkkk',100,130),('aceecgkkekmnelnoeknoelmncgklacee','aceecgkkekmnelnoeknoelmncgklacee',320,320),('giiiikkkiklmillmikmmimmmilkkgiii','giiiikkkiklmillmikmmimmmilkkgiii',330,330),('kkkklmmmjkkkjkkkjkkkjkkkjkkkkkkl','kkkklmmmjkkkjkkkjkkkjkkkjkkkkkkl',500,500),('giijikkkiklljkllkkllilllilklgiij','giijikkkiklljkllkkllilllilklgiij',900,900),('eccaeccaeccaeccageecigggookkoqmk','acegegikeioqeiqseiqseioqeekkaeee',0,0))):
 SM[7+k]=mk(a,mv,1); SM[5-k]=mk(a,mv,0); SE[7+k]=mk(b,ev,1); SE[5-k]=mk(b,ev,0)
M64=0xffffffffffffffff
_x=0x243f6a8885a308d3
def _rnd():
 global _x
 _x^=(_x<<13)&M64; _x^=_x>>7; _x^=(_x<<17)&M64; _x&=M64
 return _x
ZP=[[_rnd() for _ in range(128)] for _ in range(12)]
ZC=[_rnd() for _ in range(16)]
ZE=[_rnd() for _ in range(8)]
ZS=_rnd()
def zi(p): return p-1 if p>0 else 5-p
def sq(a,b): return ord(a)-97+(ord(b)-49)*16
B=[0]*128; W=True; CR=0; EP=-1; HM=0; H=0; MG=0; EG=0; PH=0; CW=0; CB=0; KS=[0,0]
UN=[]; TT={}; KL=[[0,0] for _ in range(128)]; HI=[0]*32768; GH=set(); PS=[]; ND=0; BG=120000; RM=0
def AT(s,w):
 for ds,pc in (((-15,-17) if w else (15,17),1),(KN,2),(KD,6)):
  q=pc if w else -pc
  for d in ds:
   t=s+d
   if not t&0x88 and B[t]==q: return 1
 g=5 if w else -5
 for ds,pc in ((BD,3),(RD,4)):
  q=pc if w else -pc
  for d in ds:
   t=s+d
   while not t&0x88:
    p=B[t]
    if p:
     if p==q or p==g: return 1
     break
    t+=d
 return 0
def CK(): return AT(KS[0 if W else 1],not W)
def IL(): return AT(KS[1 if W else 0],W)
def NX(ms,sc,i):
 bi=max(range(i,len(ms)),key=sc.__getitem__)
 if bi!=i: ms[i],ms[bi]=ms[bi],ms[i]; sc[i],sc[bi]=sc[bi],sc[i]
 return ms[i]
def G(cp):
 ms=[]; ap=ms.append
 for s in range(128):
  p=B[s]
  if not p or (p>0)!=W: continue
  a=p if p>0 else -p
  if a==1:
   d=16 if W else -16
   lr=7 if W else 0
   t=s+d
   if not t&0x88 and not B[t]:
    if (t>>4)==lr:
     for q in (5,4,3,2): ap(s|(t<<7)|(q<<14))
    elif not cp:
     ap(s|(t<<7))
     if (s>>4)==(1 if W else 6):
      t2=s+d+d
      if not B[t2]: ap(s|(t2<<7))
   for dd in (d-1,d+1):
    t=s+dd
    if t&0x88: continue
    q=B[t]
    if q and (q>0)!=W:
     if (t>>4)==lr:
      for pr in (5,4,3,2): ap(s|(t<<7)|(pr<<14))
     else: ap(s|(t<<7))
    elif t==EP: ap(s|(t<<7))
  elif a==2 or a==6:
   for d in KN if a==2 else KD:
    t=s+d
    if t&0x88: continue
    q=B[t]
    if not q:
     if not cp: ap(s|(t<<7))
    elif (q>0)!=W: ap(s|(t<<7))
   if a==6 and not cp:
    for ks,ts,rs,bt in ((4,6,7,1),(4,2,0,2),(116,118,119,4),(116,114,112,8)):
     if s==ks and CR&bt and B[rs]==(4 if W else -4):
      lo,hi=(ks,rs) if ks<rs else (rs,ks)
      ok=1
      for x in range(lo+1,hi):
       if B[x]: ok=0; break
      st=1 if ts>ks else -1
      if ok and not AT(ks,not W) and not AT(ks+st,not W) and not AT(ts,not W): ap(ks|(ts<<7))
  else:
   for d in BD if a==3 else RD if a==4 else KD:
    t=s+d
    while not t&0x88:
     q=B[t]
     if not q:
      if not cp: ap(s|(t<<7))
     else:
      if (q>0)!=W: ap(s|(t<<7))
      break
     t+=d
 return ms
def M(m):
 global W,CR,EP,HM,H,MG,EG,PH,CW,CB
 f=m&127; t=(m>>7)&127; pr=m>>14
 p=B[f]; c=B[t]; cs=t
 if not c and abs(p)==1 and t==EP:
  cs=t-16 if W else t+16; c=B[cs]
 UN.append((m,c,CR,EP,HM,H,MG,EG,PH,CW,CB))
 H^=ZP[zi(p)][f]^ZS
 if EP>=0: H^=ZE[EP&7]
 if CR: H^=ZC[CR]
 MG-=SM[6+p][f]; EG-=SE[6+p][f]
 B[f]=0
 if c:
  H^=ZP[zi(c)][cs]
  MG-=SM[6+c][cs]; EG-=SE[6+c][cs]
  a=abs(c)
  PH-=W8[a]
  if a==3:
   if c>0: CW-=1
   else: CB-=1
  B[cs]=0
 np=(pr if W else -pr) if pr else p
 B[t]=np
 H^=ZP[zi(np)][t]
 MG+=SM[6+np][t]; EG+=SE[6+np][t]
 PH+=W8[pr]
 if pr==3:
  if W: CW+=1
  else: CB+=1
 if not pr and abs(p)==6:
  KS[0 if W else 1]=t
  if abs(f-t)==2:
   if t>f: rf=t+1; rt=t-1
   else: rf=t-2; rt=t+1
   r=B[rf]; B[rf]=0; B[rt]=r
   H^=ZP[zi(r)][rf]^ZP[zi(r)][rt]
   MG+=SM[6+r][rt]-SM[6+r][rf]; EG+=SE[6+r][rt]-SE[6+r][rf]
 ep=-1
 if abs(p)==1 and abs(f-t)==32:
  g=-1 if W else 1
  if ((t&7)>0 and B[t-1]==g) or ((t&7)<7 and B[t+1]==g): ep=(f+t)//2
 EP=ep
 if ep>=0: H^=ZE[ep&7]
 CR&=CM[f]&CM[t]
 if CR: H^=ZC[CR]
 HM=0 if abs(p)==1 or c else HM+1
 W=not W
def R():
 global W,CR,EP,HM,H,MG,EG,PH,CW,CB
 m,c,CR,EP,HM,H,MG,EG,PH,CW,CB=UN.pop()
 if not m:
  W=not W; return
 f=m&127; t=(m>>7)&127; pr=m>>14
 W=not W
 np=B[t]
 if pr: B[f]=1 if W else -1; B[t]=0
 else:
  B[f]=np; B[t]=0
  if abs(np)==6:
   KS[0 if W else 1]=f
   if abs(f-t)==2:
    if t>f: B[t-1]=0; B[t+1]=4 if W else -4
    else: B[t+1]=0; B[t-2]=4 if W else -4
 if c:
  if t==EP: B[t-16 if W else t+16]=c
  else: B[t]=c
def MN():
 global W,EP,H
 UN.append((0,0,CR,EP,HM,H,MG,EG,PH,CW,CB))
 if EP>=0: H^=ZE[EP&7]
 EP=-1; W=not W; H^=ZS
def E():
 p=PH if PH<24 else 24
 d=CW-CB; mg=MG+25*d; eg=EG+40*d
 s=(mg*p+eg*(24-p))//24
 return s if W else -s
def SC(m,tm,pl):
 if m==tm: return 1<<20
 f=m&127; t=(m>>7)&127; pr=m>>14
 v=B[t]
 if v: return (1<<18)+10*V[abs(v)]-V[abs(B[f])]//16+(pr<<10)
 if pr: return (1<<18)+800+(pr<<6)
 if abs(B[f])==1 and t==EP: return (1<<18)+1000
 k=KL[pl]
 if m==k[0]: return 1<<16
 if m==k[1]: return 1<<15
 return HI[(0 if W else 16384)+(f<<7)+t]
class AB(Exception): pass
def S(d,a,b,pl):
 global ND,RM
 ND+=1
 if ND>=BG: raise AB
 if pl>110: return E()
 e=TT.get(H)
 tm=0
 if e:
  ed,ef,es,tm=e
  if ed>=d:
   es-=pl if es>90000 else -pl if es<-90000 else 0
   if ef==0: return es
   if ef==1 and es>=b: return es
   if ef==2 and es<=a: return es
 if d<=0: return Q(a,b,pl)
 ck=CK()
 if ck: d+=1
 if d>=3 and not ck and pl>0 and PH>2 and b<99000:
  MN(); s=-S(d-3,-b,-b+1,pl+1); R()
  if s>=b: return s
 ms=G(0)
 n=len(ms)
 sc=[SC(x,tm,pl) for x in ms]
 ao=a; be=-1000000; bm=ln=sr=0
 for i in range(n):
  m=NX(ms,sc,i)
  f=m&127; t=(m>>7)&127
  cp=B[t]!=0 or (abs(B[f])==1 and t==EP)
  M(m)
  if IL(): R(); continue
  ln+=1
  if HM>=100 or H in GH or H in PS: s=0
  else:
   PS.append(H)
   if sr==0: s=-S(d-1,-b,-a,pl+1)
   else:
    rd=d-1
    if d>=3 and sr>=3 and not cp and not ck: rd=d-2
    if rd<d-1:
     s=-S(rd,-a-1,-a,pl+1)
     if s>a: s=-S(d-1,-a-1,-a,pl+1)
    else: s=-S(d-1,-a-1,-a,pl+1)
    if s>a and s<b: s=-S(d-1,-b,-a,pl+1)
   PS.pop()
  R()
  sr+=1
  if s>be: be=s; bm=m
  if s>a:
   a=s
   if pl==0: RM=m
  if a>=b:
   if not cp:
    k=KL[pl]
    if m!=k[0]: k[1]=k[0]; k[0]=m
    HI[(0 if W else 16384)+(f<<7)+t]+=d*d
   break
 if ln==0: return -100000+pl if ck else 0
 ef=2 if be<=ao else 1 if be>=b else 0
 ss=be+pl if be>90000 else be-pl if be<-90000 else be
 if len(TT)>400000: TT.clear()
 TT[H]=(d,ef,ss,bm)
 return be
def Q(a,b,pl):
 global ND
 ND+=1
 if ND>=BG: raise AB
 st=E()
 if st>=b: return b
 if st>a: a=st
 if pl>110: return a
 ck=CK()
 ms=G(0 if ck else 1)
 n=len(ms)
 sc=[SC(x,0,pl) for x in ms]
 ln=0
 for i in range(n):
  m=NX(ms,sc,i)
  f=m&127; t=(m>>7)&127; pr=m>>14
  if not ck:
   vv=V[abs(B[t])]
   if pr: vv+=V[pr]
   elif not vv and t==EP: vv=100
   if st+vv+250<a: continue
  M(m)
  if IL(): R(); continue
  ln+=1
  s=-Q(-b,-a,pl+1)
  R()
  if s>a: a=s
  if a>=b: break
 if ck and ln==0: return -100000+pl
 return a
def SU(fen):
 global B,W,CR,EP,HM,H,MG,EG,PH,CW,CB,KS
 B=[0]*128
 q=fen.split()
 rw=q[0].split('/')
 for ri,row in enumerate(rw):
  r=7-ri; f=0
  for ch in row:
   if ch.isdigit(): f+=ord(ch)-48
   else:
    v='PNBRQKpnbrqk'.find(ch)
    B[r*16+f]=v+1 if v<6 else 5-v; f+=1
 W=q[1]=='w'
 CR=0
 if len(q)>2:
  for ch,bt in (('K',1),('Q',2),('k',4),('q',8)):
   if ch in q[2]: CR|=bt
 EP=-1
 if len(q)>3 and q[3]!='-':
  e=sq(q[3][0],q[3][1])
  o=-16 if W else 16
  pv=1 if W else -1
  if ((e&7)>0 and B[e+o-1]==pv) or ((e&7)<7 and B[e+o+1]==pv): EP=e
 HM=int(q[4]) if len(q)>4 else 0
 MG=EG=PH=CW=CB=H=0; wk=bk=0
 for s in range(128):
  p=B[s]
  if p:
   H^=ZP[zi(p)][s]
   MG+=SM[6+p][s]; EG+=SE[6+p][s]
   a=abs(p)
   PH+=W8[a]
   if a==3:
    if p>0: CW+=1
    else: CB+=1
   elif a==6:
    if p>0: wk=s
    else: bk=s
 KS=[wk,bk]
 if not W: H^=ZS
 if CR: H^=ZC[CR]
 if EP>=0: H^=ZE[EP&7]
 UN.clear()
def AP(u):
 pr=0
 if len(u)>4: pr='  nbrq'.index(u[4])
 M(sq(u[0],u[1])|(sq(u[2],u[3])<<7)|(pr<<14))
def UC(m):
 f=m&127; t=(m>>7)&127; pr=m>>14
 s='abcdefgh'[f&7]+'12345678'[f>>4]+'abcdefgh'[t&7]+'12345678'[t>>4]
 if pr: s+='  nbrq'[pr]
 return s
def solve(fen,mv,sf):
 global GH,PS,ND,RM
 GH=set()
 if sf and mv:
  SU(sf)
  GH.add(H)
  for u in mv:
   AP(u); GH.add(H)
 SU(fen)
 PS=[H]
 e=TT.get(H)
 br=e[3] if e else 0
 RM=br; ND=0
 try:
  for d in range(1,25):
   S(d,-1000000,1000000,0)
   br=RM
 except AB: pass
 if not br:
  for m in G(0):
   M(m)
   if not IL(): br=m; R(); break
   R()
 return UC(br) if br else ''
def post(p,o):
 q=u.Request(EV+p,data=json.dumps(o).encode(),headers={'Content-Type':'application/json'})
 with u.urlopen(q) as r: return json.load(r)
def main():
 global EV
 EV=os.environ['MAKEFUN_ENV_URL']
 cg=-1
 while True:
  try: r=post('/game',{})
  except Exception: continue
  if r.get('status')=='done': return
  lm=r.get('legal_moves')
  if not lm: continue
  g=r['game']
  if g!=cg:
   TT.clear(); cg=g
  try: mv=solve(r['fen'],r.get('moves') or [],r.get('start_fen') or '')
  except Exception: mv=''
  if mv not in lm: mv=lm[0]
  try: post('/move',{'game':g,'move':mv})
  except Exception: pass
if __name__=='__main__':main()
