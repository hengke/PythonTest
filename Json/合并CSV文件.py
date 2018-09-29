# coding = utf-8
import os

DataPath = r"E:\A1-2.0数据\单井卡片"
ff = open(r"E:\A1-2.0数据\单井卡片.csv", "w")
ff.write("WELL_ID,WELL_COMMON_NAME,WELLBORE_COMMON_NAME,WELL_PURPOSE,REASON,TARGET_FORMATION,SPUD_DATE,END_DRILLING_DATE,EGL,KB,COMPLETION_DATE,DESIGN_FORMATION,BUDGETED_MD,COMPLETION_FORMATION,COMPLETION_MD,COMPLETION_METHOD,ARTIFICIAL_WELL_BTM,W_REASON,WELLBORE_ID,WELLBORE_NO,SEISMIC_LINE_NO,DISCARDE_TYPE,GEO_DESCRIPTION,STRUCTURE_POS,GEO_OFFSET_EAST,GEO_OFFSET_NORTH,JD,WD")
ff.write("\n")
# for file in os.listdir(DataPath):
for root, dirs, files in os.walk(DataPath, topdown=False):
    for file in files:
        if os.path.splitext(file)[1] == ".csv":
            apath = os.path.join(root, file)#合并成一个完整路径
            f = open(apath, "r")
            strline = f.readlines()
            f.close()
            ff.write(strline[1])
    pass
ff.close()

print("所有CSV文件合并成功！")