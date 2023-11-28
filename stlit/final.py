
import pandas as pd
 
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv("stlit/maro_cleand.csv")
st.title('gkc')
xcc= df[df[["Place of Residence"]] != "na" ]
xc=xcc["Place of Residence"].value_counts()
x=xc.nlargest(7)



def main2():
   
    plt.figure(figsize=(15, 8))
    plt.bar(x.index,x.values , color='skyblue')
    plt.xlabel("the number")
    plt.ylabel("the site ")
    plt.title("tha most palces that gkc known from")
    plt.xticks(rotation=70)
    st.pyplot(plt)
tab1, tab2, tab3 , tab4, tab5 = st.tabs(["p1", "p2", "p3", "p4", "p5"])

with tab1:
    st.header("tha most palces that gkc known from")
    urt=st.button("click           me")
    if urt:
    
        main2()


with tab2:
    choice = st.radio("Select one option:", xc.index)

    x=df[df["Place of Residence"] == choice ]
    y=x[x["Place of Residence"] != "na" ].iloc[:,10:].sum().nlargest(5)
        

    
    
    
 
    urt2=st.button("click            me")
    if urt2:
        plt.bar(y.index, y.values)
        plt.xlabel('Courses ')  # Add x-axis label
        plt.ylabel('Count ')  # Add y-axis label
        plt.title('Course Enrollment ')  # Add title
        plt.xticks(rotation=90)
        plt.show()
        st.pyplot(plt)

with tab3:
    st.header("the top 5 courses by month")
    moto=8
    
    
    y=df[df["month"] == moto ].iloc[:,10:].sum().nlargest(7)
    
    
    urt3=st.button("click              me")
    if urt3:
        plt.bar(y.index, y.values)
        plt.xlabel('Courses ')  # Add x-axis label
        plt.ylabel('Count ')  # Add y-axis label
        plt.title('the top 5 courses by month ')  # Add title
        plt.xticks(rotation=90)


        st.pyplot(plt)
with tab4:
    st.header("the most interesting courses outside Egypt")

    x=df[df["Country"] != "eygpt"]
    y=x[x["Country"] != "na" ].iloc[:,10:].sum().nlargest(7)

    ur3=st.button("click               me")
    if ur3:
        plt.bar(y.index, y.values)
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

    x=df[df["Academic Year"] == hamra ]
    y=x[x["Academic Year"] != "na" ].iloc[:,10:].sum().nlargest(7)


    ur3=st.button("click                    me")
    if ur3:
        plt.bar(y.index, y.values)
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

    x=df[df["Learned About Genius From"] == hamraa ]
    y=x[x["Learned About Genius From"] != "na" ].iloc[:,10:].sum().nlargest(7)

    ur3=st.button("click                                    me")
    if ur3:
        plt.bar(y.index, y.values)
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
