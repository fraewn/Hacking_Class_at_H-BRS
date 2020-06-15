#include <stdint.h>

void _start(void)

{
  uint uVar1;
  
  uVar1 = main();
  syscall(0xe7,(ulong)uVar1);
  return;
}


undefined8 main(void)
{
  int iVar1;
  
  syscall(1,1,"Please give me the flag:\n",0x19);
  syscall(0,0,buf,0x40);
  iVar1 = check_flag_correct(buf);
  if (iVar1 == 0) {
    syscall(1,1,"Nope!\n",6);
    return 1;
  }
  syscall(1,1,"That is correct!\n",0x11);
  return 0;
}

ulong check_flag_correct(char *param_1)
{
  uint uVar1;
  ulong uVar2;
  long lVar3;
  byte *pbVar4;
  byte *pbVar5;
  bool bVar6;
  bool bVar7;

  if (*param_1 != 'f') {
    return 0;
  }
  if (param_1[1] != 'l') {
    return 0;
  }
  if (param_1[2] != 'a') {
    return 0;
  }
  if (param_1[3] != 'g') {
    return 0;
  }
  bVar6 = (byte)param_1[4] < 0x7b;
  bVar7 = param_1[4] == 0x7b;
  if (!bVar7) {
    return 0;
  }
  lVar3 = 0x17;
  pbVar4 = (byte *)(param_1 + 5);
  pbVar5 = (byte *)"congratulations_you_are";
  do {
    if (lVar3 == 0) break;
    lVar3 = lVar3 + -1;
    bVar6 = *pbVar4 < *pbVar5;
    bVar7 = *pbVar4 == *pbVar5;
    pbVar4 = pbVar4 + 1;
    pbVar5 = pbVar5 + 1;
  } while (bVar7);
  uVar1 = SEXT14((char)((!bVar6 && !bVar7) - bVar6));
  uVar2 = (ulong)uVar1;
  if (uVar1 == 0) {
    uVar1 = 0;
    while (uVar1 < 0x17) {
      if (((byte)strangestring[uVar1] - uVar1 & 0xff) != (int)param_1[uVar1 + 0x1c]) {
        return uVar2;
      }
      uVar1 = uVar1 + 1;
    }
    if (param_1[0x33] == '}') {
      return 1;
    }
  }
  else {
    uVar2 = 0;
  }
  return uVar2;
}


long syscall(long __sysno,...)
{
  syscall();
  return __sysno;
}
