from matplotlib import pyplot as plt
#General graph without customizing and lable 
'''apple=[200,344,345,354,400,500]  
plt.plot(apple)
plt.show()'''

#General graph without lable
'''yield_year=[2020,2021,2022,2023,2024]
yield_apple=[800,900,1200,1300,1500]
plt.plot(yield_year,yield_apple)
plt.show()'''

#General graph
'''yield_year=[2020,2021,2022,2023,2024]
yield_apple=[800,900,1200,1300,1500]
plt.plot(yield_year,yield_apple)
plt.xlabel("Year of Yield")
plt.ylabel("Total Apple Yield in form of Weight(kg)")
plt.show()'''

#General graph apple vs banana
'''yield_year=[2020,2021,2022,2023,2024]
yield_apple=[800,900,1200,1300,1500]
yield_banana=[1200,1000,1050,900,855]
plt.plot(yield_year,yield_apple)
plt.plot(yield_year,yield_banana)
plt.xlabel("Year of Yield")
plt.ylabel("Total Apple Yield in form of Weight(kg)")
plt.show()'''

#General graph which specified the color of relative data 
'''yield_year=[2020,2021,2022,2023,2024]
yield_apple=[800,900,1200,1300,1500]
yield_banana=[1200,1000,1050,900,855]
yield_orange=[1222,1321,1599,1400,1200]
plt.plot(yield_year,yield_apple)
plt.plot(yield_year,yield_banana)
plt.plot(yield_year,yield_orange)
plt.title("Graph of apple vs banana vs orange with respect to year") #Title of graph 
plt.xlabel("Year of Yield")
plt.ylabel("Total Apple Yield in form of Weight(kg)")
plt.legend(["yield_banana","yield_apple","yield_orange"])
plt.show()'''

#Graph to mark exact point
'''yield_year=[2020,2021,2022,2023,2024]
yield_apple=[800,900,1200,1300,1500]
yield_banana=[1200,1000,1050,900,855]
yield_orange=[1222,1321,1599,1400,1200]
plt.plot(yield_year,yield_apple,marker="o")
plt.plot(yield_year,yield_banana,marker="s")
plt.plot(yield_year,yield_orange,marker="p")
plt.title("Graph of apple vs banana vs orange with respect to year") 
plt.xlabel("Year of Yield")
plt.ylabel("Total Apple Yield in form of Weight(kg)")
plt.legend(["yield_banana","yield_apple","yield_orange"])
plt.show()'''

#Graph with specified color
'''yield_year=[2020,2021,2022,2023,2024]
yield_apple=[800,900,1200,1300,1500]
yield_banana=[1200,1000,1050,900,855]
yield_orange=[1222,1321,1599,1400,1200]
plt.plot(yield_year,yield_apple,marker="o",color="red") #color --> c
plt.plot(yield_year,yield_banana,marker="s",color="yellow")
plt.plot(yield_year,yield_orange,marker="p",color="orange")
plt.title("Graph of apple vs banana vs orange with respect to year")  
plt.xlabel("Year of Yield")
plt.ylabel("Total Apple Yield in form of Weight(kg)")
plt.legend(["yield_banana","yield_apple","yield_orange"])
plt.show()'''

#Graph with specified line style
'''yield_year=[2020,2021,2022,2023,2024]
yield_apple=[800,900,1200,1300,1500]
yield_banana=[1200,1000,1050,900,855]
yield_orange=[1222,1321,1599,1400,1200]
plt.plot(yield_year,yield_apple,marker="o",color="red",linestyle="-") #linestyle --> ls
plt.plot(yield_year,yield_banana,marker="s",color="yellow",linestyle="--")
plt.plot(yield_year,yield_orange,marker="p",color="orange",linestyle="")
plt.title("Graph of apple vs banana vs orange with respect to year") #Title of graph 
plt.xlabel("Year of Yield")
plt.ylabel("Total Apple Yield in form of Weight(kg)")
plt.legend(["yield_banana","yield_apple","yield_orange"])
plt.show()'''

#Graph with specified line width
'''yield_year=[2020,2021,2022,2023,2024]
yield_apple=[800,900,1200,1300,1500]
yield_banana=[1200,1000,1050,900,855]
yield_orange=[1222,1321,1599,1400,1200]
plt.plot(yield_year,yield_apple,marker="o",color="red",linestyle="-",linewidth=2) #linewidth --> lw
plt.plot(yield_year,yield_banana,marker="s",color="yellow",linestyle="--",linewidth=3)
plt.plot(yield_year,yield_orange,marker="p",color="orange",linestyle="")
plt.title("Graph of apple vs banana vs orange with respect to year") 
plt.xlabel("Year of Yield")
plt.ylabel("Total Apple Yield in form of Weight(kg)")
plt.legend(["yield_banana","yield_apple","yield_orange"])
plt.show()'''

#Graph with specified marker edge color 
'''yield_year=[2020,2021,2022,2023,2024]
yield_apple=[800,900,1200,1300,1500]
yield_banana=[1200,1000,1050,900,855]
yield_orange=[1222,1321,1599,1400,1200]
plt.plot(yield_year,yield_apple,marker="o",color="red",linestyle="-",markeredgecolor="darkblue") #markeredgedcolor --> mec
plt.plot(yield_year,yield_banana,marker="s",color="yellow",linestyle="--",markeredgecolor="darkgreen")
plt.plot(yield_year,yield_orange,marker="p",color="orange",linestyle="",markeredgecolor="darkviolet")
plt.title("Graph of apple vs banana vs orange with respect to year") 
plt.xlabel("Year of Yield")
plt.ylabel("Total Apple Yield in form of Weight(kg)")
plt.legend(["yield_banana","yield_apple","yield_orange"])
plt.show()'''

#Graph with marker edge width
'''yield_year=[2020,2021,2022,2023,2024]
yield_apple=[800,900,1200,1300,1500]
yield_banana=[1200,1000,1050,900,855]
yield_orange=[1222,1321,1599,1400,1200]
plt.plot(yield_year,yield_apple,marker="o",color="red",linestyle="-",markeredgecolor="darkblue",markeredgewidth=3) #markeredgewidth=mew
plt.plot(yield_year,yield_banana,marker="s",color="yellow",linewidth=3,markeredgecolor="darkgreen",markeredgewidth=2)
plt.plot(yield_year,yield_orange,marker="p",color="orange",linestyle="",markeredgecolor="violet",markeredgewidth=1)
plt.title("Graph of apple vs banana vs orange with respect to year") 
plt.xlabel("Year of Yield")
plt.ylabel("Total Apple Yield in form of Weight(kg)")
plt.legend(["yield_banana","yield_apple","yield_orange"])
plt.show()'''

#Graph with marker face color
'''yield_year=[2020,2021,2022,2023,2024]
yield_apple=[800,900,1200,1300,1500]
yield_banana=[1200,1000,1050,900,855]
yield_orange=[1222,1321,1599,1400,1200]
plt.plot(yield_year,yield_apple,marker="o",markeredgewidth=3,markerfacecolor="yellow") #markerfacecolor=mfc
plt.plot(yield_year,yield_banana,marker="s",markerfacecolor="orange")
plt.plot(yield_year,yield_orange,marker="p",markerfacecolor="pink")
plt.title("Graph of apple vs banana vs orange with respect to year") 
plt.xlabel("Year of Yield")
plt.ylabel("Total Apple Yield in form of Weight(kg)")
plt.legend(["yield_banana","yield_apple","yield_orange"])
plt.show()'''

#Graph with alpha
'''yield_year=[2020,2021,2022,2023,2024]
yield_apple=[800,900,1200,1300,1500]
yield_banana=[1200,1000,1050,900,855]
yield_orange=[1222,1321,1599,1400,1200]
plt.plot(yield_year,yield_apple,marker="o",alpha=1)
plt.plot(yield_year,yield_banana,marker="s",alpha=0.20)
plt.plot(yield_year,yield_orange,marker="p",alpha=0.60)
plt.title("Graph of apple vs banana vs orange with respect to year") 
plt.xlabel("Year of Yield")
plt.ylabel("Total Apple Yield in form of Weight(kg)")
plt.legend(["yield_banana","yield_apple","yield_orange"])
plt.show()'''

#Graph with grids
'''import seaborn as sns
sns.set_style("darkgrid")
yield_year=[2020,2021,2022,2023,2024]
yield_apple=[800,900,1200,1300,1500]
yield_banana=[1200,1000,1050,900,855]
yield_orange=[1222,1321,1599,1400,1200]
plt.plot(yield_year,yield_apple,marker="o",markeredgewidth=3,markerfacecolor="yellow") #markerfacecolor=mfc
plt.plot(yield_year,yield_banana,marker="s",markerfacecolor="orange")
plt.plot(yield_year,yield_orange,marker="p",markerfacecolor="pink")
plt.title("Graph of apple vs banana vs orange with respect to year") 
plt.xlabel("Year of Yield")
plt.ylabel("Total Apple Yield in form of Weight(kg)")
plt.legend(["yield_banana","yield_apple","yield_orange"])
plt.show()'''
