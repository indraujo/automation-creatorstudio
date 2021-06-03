from numpy.core.numeric import NaN
import pandas as pd

df = pd.read_excel(".\\modules\\facebookcreatorstudio\\postdata.xlsx",sheet_name="Sheet1")
account = df["account"].tolist()
path = df["path"].tolist()
image1 = df["image1"].tolist()
image2 = df["image2"].tolist()
image3 = df["image3"].tolist()
image4 = df["image4"].tolist()
image5 = df["image5"].tolist()
image6 = df["image6"].tolist()
image7 = df["image7"].tolist()
image8 = df["image8"].tolist()
image9 = df["image9"].tolist()
caption = df["caption"].tolist()
date = df["date"].tolist()
times = df["time"].tolist()
print(df)
print(len(df))
for i in range(len(df)):
    print("Account : ",account[i])
    #print("Caption : ",caption[i])
    print("Day     : ",date[i].day)
    print("Month     : ",date[i].strftime('%B'))
    print("Year     : ",date[i].year)
    print("Time Hour : ",times[i].hour)
    print("Time minutes : ",times[i].minute)
    print("Time AM/PM : ",times[i].strftime("%p"))
    print("image1 : ",type(image1[i]))
    print("image2 : ",type(image2[i]))
    print("image3 : ",type(image3[i]))
    print("image4 : ",type(image4[i]))
    print("image5 : ",type(image5[i]))
    print("image6 : ",type(image6[i]))
    print("image7 : ",type(image7[i]))
    print("image8 : ",type(image8[i]))
    print("image9 : ",type(image9[i]))


    image = []
    if pd.notna(image1[i]):
        image.append(path[i]+image1[i]+".jpg")
    if pd.notna(image2[i]):
        image.append(path[i]+image2[i]+".jpg")
    if pd.notna(image3[i]):
        image.append(path[i]+image3[i]+".jpg")
    if pd.notna(image4[i]):
        image.append(path[i]+image4[i]+".jpg")
    if pd.notna(image5[i]):
        image.append(path[i]+image5[i]+".jpg")
    if pd.notna(image6[i]):
        image.append(path[i]+image6[i]+".jpg")
    if pd.notna(image7[i]):
        image.append(path[i]+image7[i]+".jpg")
    if pd.notna(image8[i]):
        image.append(path[i]+image8[i]+".jpg")
    if pd.notna(image9[i]):
        image.append(path[i]+image9[i]+".jpg")

    print(image)