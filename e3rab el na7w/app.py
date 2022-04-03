import tkinter as tk
import re
import smtplib
import time

HEIGHT = 300
WIDTH = 400

root = tk.Tk()
root.geometry("400x300")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

root.title("اعراب الجمل")
root.iconbitmap("NahwIcon.ico")


def e3rab():
    global entry
    global label

    sentence = entry.get()
    pattern1 = "[(^ت)(^ي)]"
    pattern2 = "(^ال)"
    pattern3 = "[abcdefghijklmnopqrstuvwxyz]"
    pattern4 = "[أدجفحخهعغقثصضشسنمكطظزوةىرؤءئذل]"
    low = sentence.split(" ")
    lafzalglala = ["الله", "الرحمن", "الرحيم", "الملك", "القدوس"]
    mobtada = []
    khabar = []
    fe3l = []
    fa3el = []
    fe3lmad = []
    maf3ol_beh = []
    modafeleh = []
    tahtag_takmela = ["رئيس", "شركة", "مدير", "وزير", "جملة", "أمير", "أمر", "كثرة", "طالب", "مدرس", "شعاع"]
    sefat = ["المصري"]
    na3t = []
    tme3rab = []
    klmat_tbda2_be_ta2 = ["تعب", "توت", "تمر", "تمساح", "تاج", "تين", "تفاح"]
    hrofgar = ["من", "إلى", "الى", "في", "فى", "على", "عن", "حتى", "مذ", "منذ", "عدا", "حاشا", "خلا"]
    esmmgror = []
    asma2_tantahy_be_ta2_marbota = ["القهوة", "الفرشاة"]
    zarf_mkan_8er_mosaref = ["حول", "حول", "تجاه", "لدى", "لدن", "خلف", "وراء", "أمام", "فدام", "فوق", "تحت", "حيث",
                             "دون", "عند"]
    zarf_zman_motsaref = ["اليوم", "الليلة", "مساء", "صباحا", "بكرة", "سحرا", "لحظة", "برهة ", "ساعة", "يوم", "أسبوع",
                          "شهر", "سنة", "وقت", "مدة", "فترة", "فجرا", "ظهرا", "عصرا", "مغربا", "عشاء", "حديثا",
                          "قديما", "مساءا"]
    zarf_mabni = ["أمس", "منذ", "قط", "الآن", "إذا", "اذا", "إذ", "اذ", "حيث", "لدى", "لدن"]
    ekraa = ""
    match3 = re.match(pattern3, sentence)
    if match3:
        top1 = tk.Toplevel()
        top1.geometry("260x100")
        top1.iconbitmap("NahwIcon.ico")
        background_image3 = tk.PhotoImage(file="NahwIcon.PNG")
        background_label3 = tk.Label(top1, image=background_image3)
        background_label3.place(relwidth=1, relheight=1)
        canvass = tk.Canvas(top1, height=HEIGHT, width=WIDTH)
        canvass.pack()
        top1.title("عطل")
        background_imagee1 = tk.PhotoImage(file="Guiiyy.PNG")
        background_labele = tk.Label(top1, image=background_imagee1)
        background_labele.place(relwidth=1, relheight=1)
        framee1 = tk.Frame(top1)
        framee1.place(relwidth=1, relheight=1)
        texte1 = tk.Label(framee1, text="تأكد من عدم كتابة حرف أو كلمة واحدة فقط\n\nأو أي حروف أو كلمات غير عربية")
        texte1.place(relwidth=1, relheight=1)
    if time.sleep(0.5) and label.cget("text") == "":
        top1 = tk.Toplevel()
        top1.geometry("260x100")
        top1.iconbitmap("NahwIcon.ico")
        background_image3 = tk.PhotoImage(file="NahwIcon.PNG")
        background_label3 = tk.Label(top1, image=background_image3)
        background_label3.place(relwidth=1, relheight=1)
        canvass = tk.Canvas(top1, height=HEIGHT, width=WIDTH)
        canvass.pack()
        top1.title("عطل")
        background_imagee1 = tk.PhotoImage(file="Guiiyy.PNG")
        background_labele = tk.Label(top1, image=background_imagee1)
        background_labele.place(relwidth=1, relheight=1)
        framee1 = tk.Frame(top1)
        framee1.place(relwidth=1, relheight=1)
        texte1 = tk.Label(framee1, text="يبدو أن هناك خطأ في الجملة المكتوبة\nمن فضلك أبلغ عن الجملة")
        texte1.place(relwidth=1, relheight=1)

    for i in range(len(low)):
        match1 = re.match(pattern1, low[i])
        match2 = re.match(pattern2, low[i])
        match4 = re.match(pattern4, low[i])
        if len(low) == 1 or len(low[i]) == 1:
            top1 = tk.Toplevel()
            top1.geometry("260x100")
            top1.iconbitmap("NahwIcon.ico")
            background_image3 = tk.PhotoImage(file="NahwIcon.PNG")
            background_label3 = tk.Label(top1, image=background_image3)
            background_label3.place(relwidth=1, relheight=1)
            canvass = tk.Canvas(top1, height=HEIGHT, width=WIDTH)
            canvass.pack()
            top1.title("عطل")
            background_imagee1 = tk.PhotoImage(file="Guiiyy.PNG")
            background_labele5 = tk.Label(top1, image=background_imagee1)
            background_labele5.place(relwidth=1, relheight=1)
            framee1 = tk.Frame(top1)
            framee1.place(relwidth=1, relheight=1)
            texte1 = tk.Label(framee1, text="تأكد من عدم كتابة حرف أو كلمة واحدة فقط\n\nأو أي حروف أو كلمات غير عربية")
            texte1.place(relwidth=1, relheight=1)
        if low[i] in hrofgar and low[i] not in tme3rab:
            tme3rab.append(low[i])
            ekraa = ekraa + "\n" + low[i] + ": حرف جر "
        elif (low[i].startswith("ك") and low[i][1:3] == "ال" and low[i] not in tme3rab) \
                or (low[i].startswith("ل") and low[i][1:3] == "ال" and low[i] not in tme3rab) \
                or (low[i].startswith("ب") and low[i][1:3] == "ال" and low[i] not in tme3rab) \
                or (low[i].startswith("و") and low[i][1:5] == "الله" and low[i] not in tme3rab) \
                or (low[i].startswith("ت") and low[i][1:5] == "الله" and low[i] not in tme3rab):
            tme3rab.append(low[i])
            tme3rab.append(low[i][0])
            hrofgar.append(low[i][0])
            ekraa = ekraa + "\n" + low[i][0] + ": حرف جر "
        if low[i - 1] in hrofgar:
            if low[i] in lafzalglala:
                esmmgror.append(low[i])
                tme3rab.append(low[i])
                ekraa = ekraa + "\n" + low[i] + ": لفظ الجلالة اسم مجرور بالكسرة"
            else:
                esmmgror.append(low[i])
                tme3rab.append(low[i])
                ekraa = ekraa + "\n" + low[i] + ": اسم مجرور بالكسرة"
        elif low[i][0] in hrofgar:
            if low[i][1:5] in lafzalglala:
                esmmgror.append(low[i][1:])
                tme3rab.append(low[i][1:])
                ekraa = ekraa + "\n" + low[i][1:] + ": لفظ الجلالة اسم مجرور بالكسرة"
            else:
                esmmgror.append(low[i])
                tme3rab.append(low[i])
                ekraa = ekraa + "\n" + low[i][1:] + ": اسم مجرور بالكسرة"
        if (match2 or match4) and i == 0 and low[i].endswith("ت") is False and len(mobtada) < 1 \
                and low[i].startswith("ست") is False and low[i].endswith("ون") is False \
                and low[i].endswith("ان") is False and low[i] not in tme3rab and low[i] not in hrofgar:
            if low[i] in lafzalglala:
                mobtada.append(low[i])
                tme3rab.append(low[i])
                ekraa = ekraa + "\n" + low[i] + ": لفظ الجلالة مبتدأ مرفوع بالضمة"
            else:
                mobtada.append(low[i])
                tme3rab.append(low[i])
                ekraa = ekraa + "\n" + low[i] + ": مبتدأ مرفوع بالضمة"
        if low[i].endswith("ان") and i == 0 and low[i] not in tme3rab and low[i].startswith("ي") is False:
            mobtada.append(low[i])
            tme3rab.append(low[i])
            ekraa = ekraa + "\n" + low[i] + ": مبتدأ مرفوع وعلامة رفعه الألف\n لأنه مثنى"
        if low[i].endswith("ون") and i == 0 and low[i] not in tme3rab and low[i].startswith("ي") is False:
            mobtada.append(low[i])
            tme3rab.append(low[i])
            ekraa = ekraa + "\n" + low[i] + ": مبتدأ مرفوع وعلامة رفعه الواو\n لأنه جمع مذكر سالم"
        if (low[i-2] in hrofgar and low[i-1] in esmmgror and low[i].endswith("ون") is False
            and low[i].startswith("ي") is False and low[i].endswith("ان") is False and low[i] not in fe3l
            and low[i] not in fe3lmad and low[i-1] not in modafeleh and low[i-1] not in na3t
            and (low[i].startswith("ال") is False and low[i-2] not in low[0] and low[i] not in fe3l
                 and low[i] not in fe3lmad
                 and low[i] not in modafeleh
                 and low[i] not in na3t
                 and low[i] not in hrofgar
                 and low[i] not in zarf_zman_motsaref)) \
                or (low[i-2] in low[0] and low[i-1] in esmmgror and low[i].startswith("ي") is False
                    and low[i].endswith("ان") is False and low[i].endswith("ون") is False):
            if low[i] in lafzalglala:
                mobtada.append(low[i])
                tme3rab.append(low[i])
                ekraa = ekraa + "\n" + low[i] + ": لفظ الجلالة مبتدأ مؤخر مرفوع بالضمة"
            else:
                mobtada.append(low[i])
                tme3rab.append(low[i])
                ekraa = ekraa + "\n" + low[i] + ": مبتدأ مؤخر مرفوع بالضمة"
        if low[i-2] in hrofgar and low[i-1] in esmmgror and low[i].endswith("ان") \
                and low[i] not in fe3l and low[i] not in fe3lmad and low[i].startswith("ي") is False:
            mobtada.append(low[i])
            tme3rab.append(low[i])
            ekraa = ekraa + "\n" + low[i] + ": مبتدأ مؤخر مرفوع وعلامة رفعه الألف\n لأنه مثنى"
        if low[i-2] in hrofgar and low[i-1] in esmmgror and low[i].endswith("ون") \
                and low[i] not in fe3l and low[i] not in fe3lmad and low[i].startswith("ي") is False:
            mobtada.append(low[i])
            tme3rab.append(low[i])
            ekraa = ekraa + "\n" + low[i] + ": مبتدأ مؤخر مرفوع وعلامة رفعه الواو\n لأنه جمع مذكر سالم"
        if (low[i].endswith("ون") is False and len(mobtada) == 1 and low[i].startswith("ي") is False
            and len(fe3l) == 0 and len(fe3lmad) == 0 and low[i] not in tme3rab and len(khabar) < 1
            and low[i-1][2] == "ت" is False and low[i-1].startswith("ي") is False
            and low[i-1].startswith("ت") is False and low[i] not in zarf_mkan_8er_mosaref) \
                or (low[i] in tahtag_takmela and low[i] not in tme3rab and low[i-1].startswith("ا") is False
                    and low[i-1][2] == "ت" is False and low[i-1].startswith("ي") is False
                    and low[i-1].startswith("ت") is False and low[i] not in zarf_mkan_8er_mosaref) \
                or (low[i-1] in khabar and low[i-1].startswith("ال") is False and low[i-1][2] == "ت" is False
                    and low[i-1].startswith("ي") is False and low[i-1] not in tahtag_takmela
                    and low[i].startswith("ال") is False and low[i][2] == "ت" is False
                    and low[i].startswith("ي") is False and low[i].startswith("ت") is False
                    and low[i] not in zarf_mkan_8er_mosaref) \
                or (low[i-1] in modafeleh and low[i-2] in mobtada and low[i].startswith("ال") is False and low[i])\
                or (low[i-1] in mobtada and low[i].startswith("ال") is False and low[i-1] not in tahtag_takmela
                    and low[i-1] not in zarf_mkan_8er_mosaref and low[i] not in tme3rab
                    and low[i] not in zarf_mkan_8er_mosaref and low[i].startswith("ي") is False
                    and low[i].startswith("ت") is False and low[i-1] not in fe3l)\
                or (low[0] in mobtada and low[i-1] in khabar and low[i].startswith("ال") is False
                    and low[i].startswith("ي") is False and low[i].startswith("ت") is False
                    and low[i-1] not in tahtag_takmela and low[i-1] not in zarf_mkan_8er_mosaref
                    and low[i] not in zarf_mkan_8er_mosaref and low[i-1] not in fe3l) \
                or (low[0] in mobtada and low[i-1] not in khabar and low[i].startswith("ال") is False
                    and low[i].startswith("ي") is False and low[i].startswith("ت") is False
                    and low[i-1] not in tahtag_takmela and low[i-1] not in zarf_mkan_8er_mosaref
                    and low[i] not in tme3rab and low[i] not in zarf_mkan_8er_mosaref and low[i-1] not in fe3l):
            if low[i] in lafzalglala:
                khabar.append(low[i])
                tme3rab.append(low[i])
                ekraa = ekraa + "\n" + low[i] + ": لفظ الجلالة خبر مرفوع بالضمة"
            else:
                khabar.append(low[i])
                tme3rab.append(low[i])
                ekraa = ekraa + "\n" + low[i] + ": خبر مرفوع بالضمة"
        if low[i].startswith("ال") is False and low[i].endswith("ون") and len(mobtada) == 1 \
                and len(fe3l) == 0 and len(fe3lmad) == 0 and low[i].startswith("ي") is False and low[i] not in tme3rab:
            khabar.append(low[i])
            tme3rab.append(low[i])
            ekraa = ekraa + "\n" + low[i] + ": خبر مرفوع وعلامة رفعه الواو\n لأنه جمع مذكر سالم"
        if low[i].startswith("ال") is False and low[i].endswith("ان") and len(mobtada) == 1 \
                and len(fe3l) == 0 and len(fe3lmad) == 0 and low[i].startswith("ي") is False and low[i] not in tme3rab\
                and low[i].startswith("ي") is False:
            khabar.append(low[i])
            tme3rab.append(low[i])
            ekraa = ekraa + "\n" + low[i] + ": خبر مرفوع وعلامة رفعه الألف\n لأنه مثنى"
        if (match1 and len(fe3l) < 1 and low[i] not in tme3rab and low[i] not in klmat_tbda2_be_ta2
                and low[i].endswith("ون") is False and low[i].endswith("ان") is False) \
                or (match1 and len(fe3l) < 1 and low[i] not in tme3rab and low[i] not in klmat_tbda2_be_ta2
                    and low[i].endswith("و") and low[i].endswith("ان") is False) \
                or (match1 and len(fe3l) < 1 and low[i] not in tme3rab and low[i] not in klmat_tbda2_be_ta2
                    and low[i].endswith("ون") is False and low[i].endswith("ان") is False):
            fe3l.append(low[i])
            tme3rab.append(low[i])
            ekraa = ekraa + "\n" + low[i] + ": فعل مضارع مرفوع بالضمة"
        if (low[i].startswith("ي") and low[i].endswith("ان") and len(fe3l) < 1 and low[i] not in tme3rab
            and low[i] not in klmat_tbda2_be_ta2) \
                or (low[i].startswith("ت") and low[i].endswith("ان") and len(fe3l) < 1 and low[i] not in tme3rab
                    and low[i] not in klmat_tbda2_be_ta2):
            fe3l.append(low[i])
            tme3rab.append(low[i])
            ekraa = ekraa + "\n" + low[i] + ": فعل مضارع مرفوع بثبوت النون\nلأنه من الأفعال الخمسة"
        if (low[i-1].endswith("ان") and low[i-1] in fe3l and len(fa3el) < 1 and low[i-1] not in fa3el
                and len(maf3ol_beh) < 1):
            fa3el.append("alfnon")
            ekraa = ekraa + " وألف الاثنين ضمير \nمتصل مبني في محل رفع فاعل"
        if (low[i].startswith("ي") and low[i].endswith("ون") and len(fe3l) < 1 and low[i] not in tme3rab
            and low[i] not in klmat_tbda2_be_ta2) \
                or (low[i].startswith("ت") and low[i].endswith("ون") and len(fe3l) < 1 and low[i] not in tme3rab
                    and low[i] not in klmat_tbda2_be_ta2):
            fe3l.append(low[i])
            tme3rab.append(low[i])
            ekraa = ekraa + "\n" + low[i] + ": فعل مضارع مرفوع بثبوت النون\nلأنه من الأفعال الخمسة"
        if (low[i-1].endswith("ون") and low[i-1] in fe3l and len(fa3el) < 1 and len(maf3ol_beh) < 1) \
                or (low[i-1].endswith("و") and low[i-1] in fe3l and len(fa3el) < 1 and len(maf3ol_beh) < 1):
            fa3el.append("waw")
            ekraa = ekraa + " والواو ضمير\n متصل مبني في محل رفع فاعل"
        if low[i].startswith("ست") and low[i].endswith("ون"):
            fe3l.append(low[i])
            tme3rab.append(low[i])
            ekraa = ekraa + "\n" + low[i] + ": فعل مضارع مرفوع بثبوت النون والواو \n ضمير متصل مبني في محل رفع فاعل"
        if low[i-1].startswith("ست") and low[i-1].endswith("ون") and i-1 != 0:
            khabar.append(low[i])
            tme3rab.append(low[i])
            ekraa = ekraa + "\n" + "والجملة الفعلية في محل رفع خبر"
        if (low[i].endswith("ات") is False and low[i].endswith("ت") and low[i] not in tme3rab
            and low[i] not in klmat_tbda2_be_ta2 and len(fe3lmad) < 1) or (low[i].endswith("ات") is False
                                                                           and low[i].endswith("ت")
                                                                           and low[i] not in tme3rab
                                                                           and low[i] not in klmat_tbda2_be_ta2
                                                                           and len(fe3lmad) < 1) \
                or (low[i].endswith("ات") is False and low[i].startswith("ا")
                    and low[i].endswith("ت") and low[i][2] == "ت" and low[i] not in tme3rab
                    and low[i] not in klmat_tbda2_be_ta2 and len(fe3lmad) < 1):
            fe3lmad.append(low[i])
            tme3rab.append(low[i])
            ekraa = ekraa + "\n" + low[i] + ": فعل ماض مبني على الفتح"
        if (low[i].startswith("ي") is False and low[i].startswith("ت") is False and len(fe3l) > 0
            and re.match(pattern1, low[i - 1]) and len(mobtada) != 1 and low[i] not in tme3rab
            and i-1 == 0) or (low[i].startswith("ي") is False and low[i].startswith("ت") is False and len(fe3l) > 0
                              and re.match(pattern1, low[i - 1]) and len(mobtada) != 1 and low[i] not in tme3rab) \
                or (low[i].endswith("ة") and low[i - 1].endswith("ت") and "ta2" not in fa3el and len(fa3el) < 1
                    and len(mobtada) != 1 and low[i] not in asma2_tantahy_be_ta2_marbota and low[i] not in tme3rab) \
                and low[i - 1] not in hrofgar:
            if low[i] in lafzalglala:
                fa3el.append(low[i])
                tme3rab.append(low[i])
                ekraa = ekraa + "\n" + low[i] + ": لفظ الجلالة فاعل مرفوع بالضمة"
            else:
                fa3el.append(low[i])
                tme3rab.append(low[i])
                ekraa = ekraa + "\n" + low[i] + ": فاعل مرفوع بالضمة"
        if (low[i-1] in fe3lmad and len(fa3el) < 1 and low[i-1] not in fa3el and len(tme3rab) == 1
                and len(maf3ol_beh) < 1):
            fa3el.append("ta2")
            ekraa = ekraa + " والتاء ضمير\n متصل مبني في محل رفع فاعل"
        if (low[i - 1] in fa3el and low[i - 2] in fe3l and low[i] not in tme3rab and low[i] not in hrofgar
            and low[i] not in sefat and i == -1 and low[i] not in zarf_mkan_8er_mosaref) \
                or (low[i - 1] in fe3l and low[i - 2] in mobtada and low[i] not in tme3rab and low[i] not in hrofgar
                    and low[i] not in sefat and low[i] not in zarf_mkan_8er_mosaref) \
                or (low[i - 1] in fe3l and low[i - 2] in mobtada and low[i] not in tme3rab and low[i] not in hrofgar
                    and low[i] not in sefat and low[i] not in zarf_mkan_8er_mosaref) \
                or (low[i - 1] in fa3el and low[i - 2] in fe3lmad and low[i] not in tme3rab and low[i] not in hrofgar
                    and low[i] not in sefat and low[i] not in zarf_mkan_8er_mosaref) \
                or ("ta2" in fa3el and low[i - 1] in fe3lmad and low[i] not in tme3rab and low[i] not in hrofgar
                    and low[i] not in sefat and low[i] not in zarf_mkan_8er_mosaref) \
                or (low[i-1] in na3t and low[i-2] in fa3el and (low[i-3] in fe3lmad or low[i-3] in fe3l)
                    and low[i] not in tme3rab and low[i] not in zarf_mkan_8er_mosaref)\
                or (low[i - 1] in fa3el and low[i - 2] in fe3l and low[i] not in tme3rab and low[i] not in hrofgar
                    and low[i] not in sefat and low[i] not in zarf_mkan_8er_mosaref) \
                or (low[i - 1] in fe3l and low[i] not in tme3rab and low[i] not in hrofgar and low[i] not in sefat
                    and low[i] not in zarf_mkan_8er_mosaref and low[i-1] not in low[0]):
            if low[i] in lafzalglala:
                maf3ol_beh.append(low[i])
                tme3rab.append(low[i])
                ekraa = ekraa + "\n" + low[i] + ": لفظ الجلالة مفعول به منصوب بالفتحة"
            else:
                maf3ol_beh.append(low[i])
                tme3rab.append(low[i])
                ekraa = ekraa + "\n" + low[i] + ": مفعول به منصوب بالفتحة"
        if match2 and low[i - 1] in fe3lmad and len(maf3ol_beh) < 1 and len(fa3el) < 1 and low[i] not in tme3rab \
                and low[i - 1] not in hrofgar:
            fa3el.append("ta2")
            maf3ol_beh.append(low[i])
            tme3rab.append(low[i])
            ekraa = ekraa + "\n" + "و التاء ضمير متصل مبني في محل رفع فاعل"
            ekraa = ekraa + "\n" + low[i] + ": مفعول به منصوب بالفتحة"
        if low[i] in zarf_mkan_8er_mosaref:
            tme3rab.append(low[i])
            ekraa = ekraa + "\n" + low[i] + ": ظرف مكان منصوب بالفتحة"
        if low[i] in zarf_zman_motsaref and low[i] not in mobtada and low[i] not in fa3el:
            tme3rab.append(low[i])
            ekraa = ekraa + "\n" + low[i] + ": ظرف زمان منصوب بالفتحة"
        if (low[i].startswith("ال") and low[i-1].startswith("ال") and low[i] not in tme3rab and low[i-1] in mobtada
            and low[i-1] not in tahtag_takmela) \
                or (low[i].startswith("ال") and low[i-1].startswith("ال") and low[i] not in tme3rab and
                    low[i-1] in khabar and low[i-1] not in tahtag_takmela) \
                or (low[i].startswith("ال") and low[i-1].startswith("ال") and low[i] not in tme3rab
                    and low[i-1] in fa3el and low[i] in sefat) or (low[i].startswith("ال")
                                                                   and low[i-1].startswith("ال")
                                                                   and low[i] not in tme3rab
                                                                   and low[i-1] in tahtag_takmela
                                                                   and low[i-1] in khabar
                                                                   and low[i] in low[-1]) \
                or (low[i].startswith("ال") is False and low[i-1].startswith("ال") is False and low[i] not in tme3rab
                    and low[i-1] in mobtada and low[i-1] not in tahtag_takmela) \
                or (low[i].startswith("ال") is False and low[i - 1].startswith("ال") is False and low[i] not in tme3rab
                    and low[i-1] in fa3el and low[i] in sefat) \
                or (low[i].startswith("ال") is False and low[i-1].startswith("ال") is False and low[i] not in tme3rab
                    and low[i-1] in khabar and low[i-1] in tahtag_takmela and low[0] in mobtada and len(low) == 3) \
                or (low[i].startswith("ال") is False and low[i-1].startswith("ال") is False and low[i] not in tme3rab
                    and low[i-1] in khabar and low[i-1] in tahtag_takmela and low[0] in mobtada and low[i] == low[-1]) \
                or (low[i].startswith("ال") is False and low[i - 1].startswith("ال") is False and low[i] not in tme3rab
                    and low[i-1] in fa3el and low[i-1] not in tahtag_takmela):
            if low[i] in lafzalglala:
                na3t.append(low[i])
                tme3rab.append(low[i])
                ekraa = ekraa + "\n" + low[i] + ": لفظ الجلالة نعت مرفوع بالضمة"
            else:
                na3t.append(low[i])
                tme3rab.append(low[i])
                ekraa = ekraa + "\n" + low[i] + ": نعت مرفوع بالضمة"
        if (low[i].startswith("ال") and low[i-1].startswith("ال") and low[i] not in tme3rab
            and (low[i-1] in esmmgror or low[i-1] in modafeleh or low[i-1] in modafeleh and low[i] in sefat)) \
                or (low[i].startswith("ال") is False and low[i-1].startswith("ال") is False
                    and low[i] not in tme3rab and (low[i-1] in esmmgror or low[i-1] in modafeleh)):
            if low[i] in lafzalglala:
                na3t.append(low[i])
                tme3rab.append(low[i])
                ekraa = ekraa + "\n" + low[i] + ": لفظ الجلالة نعت مجرور بالكسرة"
            else:
                na3t.append(low[i])
                tme3rab.append(low[i])
                ekraa = ekraa + "\n" + low[i] + ": نعت مجرور بالكسرة"

        if (low[i].startswith("ال") and low[i-1].startswith("ال") and low[i] not in tme3rab
            and low[i-1] in maf3ol_beh and low[i-1] not in tahtag_takmela) \
                or (low[i].startswith("ال") is False and low[i-1].startswith("ال") is False
                    and low[i] not in tme3rab and (low[i-1] in maf3ol_beh and low[i-1] not in tahtag_takmela)):
            if low[i] in lafzalglala:
                na3t.append(low[i])
                tme3rab.append(low[i])
                ekraa = ekraa + "\n" + low[i] + ": لفظ الجلالة نعت منصوب بالفتحة"
            else:
                na3t.append(low[i])
                tme3rab.append(low[i])
                ekraa = ekraa + "\n" + low[i] + ": نعت منصوب بالفتحة"
        if (low[i] != low[i-1] and low[i].startswith("ال")
            and low[i-1] not in fe3l and low[i-1] not in fe3lmad and i != 0 and low[i] not in tme3rab
            and low[i] not in sefat) \
                or (low[i-1] in tahtag_takmela and (low[i-1] in khabar and low[i-2] in mobtada or low[i-1] in mobtada)
                    and low[i].endswith("ية") is False and low[i] not in tme3rab and low[i] not in sefat)\
                or (low[i-1] in tahtag_takmela and low[i-1] in khabar and low[i] not in low[-1]
                    and low[i] not in tme3rab)\
                or (low[i-1] in zarf_zman_motsaref and low[i] not in fe3l and low[i] not in fe3lmad
                    and low[i] not in tme3rab) \
                or (low[i-1] in zarf_mkan_8er_mosaref and low[i] not in fe3l and low[i] not in fe3lmad
                    and low[i] not in tme3rab) \
                or (low[i-1] in zarf_mabni and low[i] not in fe3l and low[i] not in fe3lmad and low[i] not in tme3rab)\
                or (low[i-1] in mobtada and low[i].startswith("ال") and low[i] not in tme3rab):
            if low[i] in lafzalglala:
                modafeleh.append(low[i])
                tme3rab.append(low[i])
                ekraa = ekraa + "\n" + low[i] + ": لفظ الجلالة مضاف إليه مجرور بالكسرة"
            else:
                modafeleh.append(low[i])
                tme3rab.append(low[i])
                ekraa = ekraa + "\n" + low[i] + ": مضاف إليه مجرور بالكسرة"
        label.config(text=ekraa, anchor="ne")


def send_report():
    global entry
    global label

    reports = entry.get()
    gomlreport = label.cget("text")
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login("Drakth5364", "abdoabdo5364")
    mail.sendmail("Drakth5364@gmail.com", "Drakth5364@gmail.com",
                  "Subject:اعراب الجمل: اعرابات خاطئة\n\n\nتم ارسالها من أحد المستخدمين\n\nالجملة: {0}\n\n:الاعراب\n{1}"
                  .format(reports, gomlreport).encode("UTF-8"))
    mail.quit()
    if True:
        top = tk.Toplevel()
        top.geometry("260x100")
        top.iconbitmap("NahwIcon.ico")
        background_image2 = tk.PhotoImage(file="NahwIcon.PNG")
        background_label2 = tk.Label(top, image=background_image2)
        background_label2.place(relwidth=1, relheight=1)

        canvass = tk.Canvas(top, height=HEIGHT, width=WIDTH)
        canvass.pack()

        top.title("الابلاغ عن الجملة")
        background_imagee = tk.PhotoImage(file="Guiiyy.PNG")
        background_labele = tk.Label(top, image=background_imagee)
        background_labele.place(relwidth=1, relheight=1)

        framee = tk.Frame(top)
        framee.place(relwidth=1, relheight=1)

        texte = tk.Label(framee, text="تم ارسال الجملة للمراجعة")
        texte.place(relwidth=1, relheight=1)


def credit():
    global label

    topc = tk.Toplevel()
    topc.geometry("290x130")
    topc.iconbitmap("NahwIcon.ico")
    background_imagec = tk.PhotoImage(file="NahwIcon.PNG")
    background_labelc = tk.Label(topc, image=background_imagec)
    background_labelc.place(relwidth=1, relheight=1)

    canvass = tk.Canvas(topc, height=HEIGHT, width=WIDTH)
    canvass.pack()

    topc.title("credits")
    background_imagec = tk.PhotoImage(file="Guiiyy.PNG")
    background_labelc = tk.Label(topc, image=background_imagec)
    background_labelc.place(relwidth=1, relheight=1)

    framec = tk.Frame(topc)
    framec.place(relwidth=1, relheight=1)

    textc = tk.Label(framec, text="تمت برمجة هذا البرنامج بواسطة\n"
                                  "عبدالرحمن صبري\n Drakth5364@gmail.com :للتواصل معه")
    textc.place(relwidth=1, relheight=1)


backframe = tk.Frame(root, bg="#FCF4E3")
backframe.place(relwidth=1, relheight=1)


background_image = tk.PhotoImage(file="Guiiyy.PNG")
background_label = tk.Label(backframe, image=background_image)
background_label.place(relwidth=1, relheight=1)
background_label.pack(expand=True)

frame = tk.Frame(root, bg="#271203", bd=3)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, bg="#F4D5BE")
entry.place(relwidth=0.68, relheight=1)

lower_frame = tk.Frame(root, bg="#271203", bd=3)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

lower2_frame = tk.Frame(root, bg="#271203", bd=2)
lower2_frame.place(relx=0.22, rely=0.98, relwidth=0.25, relheight=0.1, anchor="s")

lower3_frame = tk.Frame(root, bg="#FCF4E3")
lower3_frame.place(relx=0.73, rely=0.90, relwidth=0.12, relheight=0.06, anchor="n")

lower4_frame = tk.Frame(root, bg="#271203", bd=1)
lower4_frame.place(relx=0.88, rely=0.98, relwidth=0.14, relheight=0.08, anchor="s")

label = tk.Label(lower_frame, bg="#F4D5BE", font="bold 13")
label.place(relwidth=1, relheight=1)

button = tk.Button(frame, text="اعرب الجملة", font="bold", bg="#9D7A60", command=e3rab)
button.place(relx=0.7, rely=0.0, relwidth=0.3, relheight=1.05)

button2 = tk.Button(lower2_frame, text="الابلاغ عن الجملة", font=40, bg="#9D7A60", fg="#271203", command=send_report)
button2.place(relwidth=1, relheight=1)

button3 = tk.Button(lower4_frame, text="credits", font=40, bg="#9D7A60", fg="#271203", command=credit)
button3.place(relwidth=1, relheight=1)

version = tk.Label(lower3_frame, text="v.0.2", bg="#FCF4E3", font="5")
version.place(relwidth=1, relheight=1)

root.mainloop()
