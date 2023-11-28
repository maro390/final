
import pandas as pd
 
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv("stlit/maro_cleand.csv")
st.title('gkc')
popi= df[df[["Place of Residence"]] != "na" ]
yui=popi["Place of Residence"].value_counts().sort_values(ascending=False)
xc=yui.sort_values(ascending=False)
x=xc.head(7)





def delivery(nmo):
    global values, labels
   
    values = []
    labels = []
    German = [ahmsd_mphsen("German Language Course"),'German Language Course']
    Specialized_Programming = [ahmsd_mphsen("Specialized Programming Diploma"),"Specialized Programming Diploma"]
    Reader = [ahmsd_mphsen("Cultured Reader"),"Cultured Reader"]
    Mathematics = [ahmsd_mphsen("Mathematics (Matific)"),"Mathematics (Matific)"]

    Fundamentals_of_Programming = [ahmsd_mphsen("Fundamentals of Programming"),"Fundamentals_of_Programming"]
    German_Explorer = [ahmsd_mphsen("German Explorer"),"German Explorer"]

    Online_School = [ahmsd_mphsen("Online School"),"Online School"]
    Digital_Marketing_Diploma = [ahmsd_mphsen("Digital Marketing Diploma"),"Digital Marketing Diploma"]
    Graphics_Diploma = [ahmsd_mphsen("Graphics Diploma"),"Graphics Diploma"]
    Little_Explorer = [ahmsd_mphsen("Little Explorer"),"Little Explorer"]
    namy=[German,Specialized_Programming,Reader,Mathematics,Fundamentals_of_Programming,German_Explorer,Online_School,Digital_Marketing_Diploma
         ,Graphics_Diploma,Little_Explorer]
    for i in namy:

        if i[0] > nmo:
        
            values.append(i[0])
            labels.append(i[1])



# ##############################################









def main2():
   
    plt.figure(figsize=(15, 8))
    plt.bar(x.index,x.values , color='skyblue')
    plt.xlabel("the number")
    plt.ylabel("the site ")
    plt.title("tha most palces that gkc known from")
    plt.xticks(rotation=70)
    st.pyplot(plt)
tab1, tab2, tab3 , tab4, tab5 = st.tabs(["part 1", "part 2", "part 3", "part 4", "part 5"])

with tab1:
    st.header("tha most palces that gkc known from")
    urt=st.button("click           me")
    if urt:
    
        main2()


with tab2:
    st.header("tha place that enroll in corse")
    choice = st.radio("Select one option:", xc.index)
    def ahmsd_mphsen(hmasa):
        x=df[df["Place of Residence"] == choice ]
        y=x[x["Place of Residence"] != "na" ]
        return y[f"{hmasa}"].sum()
    
    delivery(0.75)
    urt2=st.button("click            me")
    if urt2:
        plt.bar(labels, values)
        plt.xlabel('Courses ')  # Add x-axis label
        plt.ylabel('Count ')  # Add y-axis label
        plt.title('Course Enrollment ')  # Add title
        plt.xticks(rotation=90)
        plt.show()
        st.pyplot(plt)

with tab3:
    st.header("the top 5 courses by month")
    moto=8
    def ahmsd_mphsen(hmasa):
    
        y=df[df["month"] == moto ]
        return y[f"{hmasa}"].sum()
    delivery(25)
    urt3=st.button("click              me")
    if urt3:
        plt.bar(labels, values)
        plt.xlabel('Courses ')  # Add x-axis label
        plt.ylabel('Count ')  # Add y-axis label
        plt.title('the top 5 courses by month ')  # Add title
        plt.xticks(rotation=90)


        st.pyplot(plt)
with tab4:
    st.header("the most interesting courses outside Egypt")
    def ahmsd_mphsen(hmasa):
        x=df[df["Country"] != "eygpt" ]
        y=x[x["Country"] != "na" ]
        return y[f"{hmasa}"].sum()
    delivery(1.5)
    ur3=st.button("click               me")
    if ur3:
        plt.bar(labels, values)
        plt.xlabel('Courses ')  # Add x-axis label
        plt.ylabel('Count ')  # Add y-axis label
        plt.title('Course Enrollment ')  # Add title
        plt.xticks(rotation=90)

    
        st.pyplot(plt)
with tab5:
    st.header("percentage of people are interested in distance learning")
    r3=st.button("click                me")
    if r3:
        homa=df["Is Online Education Useful?"].value_counts()

    # Create the pie chart
        plt.pie(homa.values, labels=homa.index, autopct='%1.1f%%')

        # Add a title
        plt.title('Pie Chart')

        # Display the chart
        st.pyplot(plt)

st.title('bouns part')


tab11,tab22,tab33,tab44,tab55 = st.tabs(["b1","b2","b3","b4","b5"])
the_age=df["Academic Year"].value_counts().sort_values(ascending=False)
with tab11:
    st.header("What is the most level to enter the site?")
    
    rr3=st.button("click                  me")
    if rr3:

        

    # Create the pie chart
        plt.bar(the_age.index,the_age.values)

        # Add a title
        plt.title('Pie Chart')
        plt.xticks(rotation=90)

        # Display the chart
        st.pyplot(plt)
with tab22:
    st.header("What are the relevant courses for each age")
    hamra=st.radio("choice",the_age.index)
    def ahmsd_mphsen(hmasa):
        x=df[df["Academic Year"] == hamra ]
        y=x[x["Academic Year"] != "na" ]
        return y[f"{hmasa}"].sum()
    delivery(.5)
    ur3=st.button("click                    me")
    if ur3:
        plt.bar(labels, values)
        plt.xlabel('Courses ')  # Add x-axis label
        plt.ylabel('Count ')  # Add y-axis label
        plt.title('Course Enrollment ')  # Add title
        plt.xticks(rotation=90)

    
        st.pyplot(plt)
the_sitee=df["Learned About Genius From"].value_counts().sort_values(ascending=False)
with tab33:
    st.header("The site where people come the most from")
    
    rr3=st.button("click                             me")
    if rr3:

        

    # Create the pie chart
        plt.bar(the_sitee.index,the_sitee.values)

        # Add a title
        plt.title('Pie Chart')
        plt.xticks(rotation=90)

        # Display the chart
        st.pyplot(plt)
with tab44:
    st.header("The site where people come the most from")
    hamraa=st.radio("choice",the_sitee.index)
    def ahmsd_mphsen(hmasa):
        x=df[df["Learned About Genius From"] == hamraa ]
        y=x[x["Learned About Genius From"] != "na" ]
        return y[f"{hmasa}"].sum()
    delivery(.5)
    ur3=st.button("click                                    me")
    if ur3:
        plt.bar(labels, values)
        plt.xlabel('Courses ')  # Add x-axis label
        plt.ylabel('Count ')  # Add y-axis label
        plt.title('Course Enrollment ')  # Add title
        plt.xticks(rotation=90)

    
        st.pyplot(plt)
with tab55:
    st.header("What is the most level to enter the site? from")
    hamraaa=st.radio("choice    ",the_sitee.index)
    x=df[df["Learned About Genius From"] == hamraaa ]
    
    homaa=x["Is Online Education Useful?"].value_counts()
    
    r3=st.button("click                                          me")
    if r3:
        
    # Create the pie chart
        plt.pie(homaa.values, labels=homaa.index, autopct='%1.1f%%')

        # Add a title
        plt.title('Pie Chart')

        # Display the chart
        st.pyplot(plt)
