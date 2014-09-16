TLK-v1-file-parser-for-Python
=============================

Parse tlk (v1) file format in Python for games like Baldur's Gate (EE), Icewind Dale and etc.
This script currently only supports tlk v1 format. So don't use it for games like NWN.

Before you start, backup your original tlk file. Read the example below and read all the comments in the script.

An example for BG:EE en-US dialog.tlk:
```
>>> dialog=readialog('dialog.tlk')
>>> for ent in dialog[:5]: print(ent)
... 
(0, 5, b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 0, 118, "Someone disturbs me?! I have no time to talk with you, <CHARNAME>. Don't take it personally. I'm just a very busy man.")
(1, 1, b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 118, 63, 'Why hast thou disturbed me here? Hast thou no manners? Get out!')
(2, 5, b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 181, 307, "So, <CHARNAME>, you have sullied your father's name by defiling his home and bringing ruin to a peace that has lasted for centuries. I spit on you and all of your friends. Your transgressions will be punished in the most severe form. I formally accuse you of the murders of Brunos Costak and Rieltar Anchev.")
(3, 1, b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 488, 228, 'Why have I accused you? You were seen fleeing the murder scene. Koveras found the identifying ring of a Shadow Thief assassin in your personal effects, and gold minted in Amn. I feel that it is strong enough proof to accuse you.')
(4, 1, b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', 716, 75, 'You were seen fleeing the site of the murder by the guest known as Koveras.')
>>> 
>>> #In this example, the dialog has not been changed. In reality, you can manipulate your dialog here. 
... 
>>> refreshdialog(dialog)
>>> writedialog(dialog,'dialog_new.tlk')
>>> #All the functions in this script won't change the dialog content by themselves.
... 
>>> import filecmp
>>> filecmp.cmp('dialog.tlk','dialog_new.tlk',shallow=False)
True
```


