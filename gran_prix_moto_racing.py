# -*- coding: utf-8 -*-
"""Gran_Prix_Moto_Racing.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17JOlwjxTTDxR70hgBBSku4DrNs7fnoLg
"""

from io import StringIO
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import markers
import seaborn as sns
import plotly.express as px

"""Link para acesso

https://rtrsports.com/en/blog/motogp-list-constructors-champions/
"""

winners_data = """
Season	Constructor	Class
2022	Ducati	MotoGP™
2022	Kalex	Moto2™
2022	GasGas	Moto3™
2022	Energica	MotoE™
2021	Yamaha	MotoGP™
2021	Kalex	Moto2™
2021	KTM	Moto3™
2021	Energica	MotoE™
2020	Suzuki	MotoGP™
2020	Kalex	Moto2™
2020	KTM	Moto3™
2020	Energica	MotoE™
2019	Honda	MotoGP™
2019	Kalex	Moto2™
2019	Honda	Moto3™
2019	Energica	MotoE™
2018	Honda	MotoGP™
2018	Kalex	Moto2™
2018	Honda	Moto3™
2017	Honda	MotoGP™
2017	Kalex	Moto2™
2017	Honda	Moto3™
2016	Honda	MotoGP™
2016	Kalex	Moto2™
2016	KTM	Moto3™
2015	Yamaha	MotoGP™
2015	Kalex	Moto2™
2015	Honda	Moto3™
2014	Honda	MotoGP™
2014	Kalex	Moto2™
2014	Honda	Moto3™
2013	Honda	MotoGP™
2013	Kalex	Moto2™
2013	KTM	Moto3™
2012	Yamaha	MotoGP™
2012	Suter	Moto2™
2012	KTM	Moto3™
2011	Honda	MotoGP™
2011	Kalex	Moto2™
2011	Aprilia	125cc
2010	Yamaha	MotoGP™
2010	Moriwaki	Moto2™
2010	Derbi	125cc
2009	Yamaha	MotoGP™
2009	Honda	250cc
2009	Aprilia	125cc
2008	Yamaha	MotoGP™
2008	Gilera	250cc
2008	Derbi	125cc
2007	Ducati	MotoGP™
2007	Aprilia	250cc
2007	Aprilia	125cc
2006	Honda	MotoGP™
2006	Aprilia	250cc
2006	Aprilia	125cc
2005	Yamaha	MotoGP™
2005	Honda	250cc
2005	Honda	125cc
2004	Yamaha	MotoGP™
2004	Honda	250cc
2004	Honda	125cc
2003	Honda	MotoGP™
2003	Aprilia	250cc
2003	Honda	125cc
2002	Honda	MotoGP™
2002	Aprilia	250cc
2002	Aprilia	125cc
2001	Honda	MotoGP™
2001	Honda	250cc
2001	Gilera	125cc
2000	Suzuki	MotoGP™
2000	Yamaha	250cc
2000	Aprilia	125cc
1999	Honda	500cc
1999	Aprilia	250cc
1999	Honda	125cc
1998	Honda	500cc
1998	Aprilia	250cc
1998	Honda	125cc
1997	Honda	500cc
1997	Honda	250cc
1997	Aprilia	125cc
1996	Honda	500cc
1996	Aprilia	250cc
1996	Honda	125cc
1995	Honda	500cc
1995	Aprilia	250cc
1995	Honda	125cc
1994	Honda	500cc
1994	Aprilia	250cc
1994	Aprilia	125cc
1993	Suzuki	500cc
1993	Yamaha	250cc
1993	Honda	125cc
1992	Yamaha	500cc
1992	Honda	250cc
1992	Aprilia	125cc
1991	Yamaha	500cc
1991	Honda	250cc
1991	Honda	125cc
1990	Yamaha	500cc
1990	Yamaha	250cc
1990	Honda	125cc
1989	Honda	500cc
1989	Honda	250cc
1989	JJ Cobas	125cc
1989	Derbi	80cc
1988	Yamaha	500cc
1988	Honda	250cc
1988	Derbi	125cc
1988	Derbi	80cc
1987	Honda	500cc
1987	Honda	250cc
1987	Garelli	125cc
1987	Derbi	80cc
1986	Yamaha	500cc
1986	Yamaha	250cc
1986	Garelli	125cc
1986	Derbi	80cc
1985	Honda	500cc
1985	Honda	250cc
1985	Garelli	125cc
1985	Krauser	80cc
1984	Yamaha	500cc
1984	Chevallier	250cc
1984	Garelli	125cc
1984	Zundapp	80cc
1983	Honda	500cc
1983	Yamaha	250cc
1983	Garelli	125cc
1983	Krauser	50cc
1982	Suzuki	500cc
1982	Yamaha	250cc
1982	Garelli	125cc
1982	Kawasaki	350cc
1982	Kreidler	50cc
1981	Suzuki	500cc
1981	Kawasaki	250cc
1981	Minarelli	125cc
1981	Kawasaki	350cc
1981	Motul Bultaco	50cc
1980	Yamaha	500cc
1980	Kawasaki	250cc
1980	MBA	125cc
1980	Bimota-Yamaha	350cc
1980	Kreidler Van Veen	50cc
1979	Yamaha	500cc
1979	Kawasaki	250cc
1979	Minarelli	125cc
1979	Kawasaki	350cc
1979	Kreidler	50cc
1978	Yamaha	500cc
1978	Kawasaki	250cc
1978	MBA	125cc
1978	Kawasaki	350cc
1978	Bultaco	50cc
1977	Suzuki	500cc
1977	Morbidelli	250cc
1977	Morbidelli	125cc
1977	Yamaha	350cc
1977	Bultaco	50cc
1976	Suzuki	500cc
1976	Harley Davidson	250cc
1976	Morbidelli	125cc
1976	Harley Davidson	350cc
1976	Bultaco	50cc
1975	Yamaha	500cc
1975	Harley Davidson	250cc
1975	Morbidelli	125cc
1975	Yamaha	350cc
1975	Kreidler	50cc
1974	MV Agusta	500cc
1974	Harley Davidson	250cc
1974	Yamaha	125cc
1974	Yamaha	350cc
1974	Van Veen-Kreidler	50cc
1973	MV Agusta	500cc
1973	Yamaha	250cc
1973	Yamaha	125cc
1973	MV Agusta	350cc
1973	Kreidler	50cc
1972	Honda	500cc
1972	Yamaha	250cc
1972	Derbi	125cc
1972	MV Agusta	350cc
1972	Kreidler	50cc
1971	MV Agusta	500cc
1971	Yamaha	250cc
1971	Derbi	125cc
1971	MV Agusta	350cc
1971	Kreidler	50cc
1970	MV Agusta	500cc
1970	Yamaha	250cc
1970	Suzuki	125cc
1970	Benelli	350cc
1970	Derbi	50cc
1969	MV Agusta	500cc
1969	Benelli	250cc
1969	Kawasaki	125cc
1969	MV Agusta	350cc
1969	Derbi	50cc
1968	MV Agusta	500cc
1968	Yamaha	250cc
1968	Yamaha	125cc
1968	MV Agusta	350cc
1968	Suzuki	50cc
1967	Honda	500cc
1967	Honda	250cc
1967	Yamaha	125cc
1967	Honda	350cc
1967	Suzuki	50cc
1966	MV Agusta	500cc
1966	Honda	250cc
1966	Honda	125cc
1966	Honda	350cc
1966	Suzuki	50cc
1965	MV Agusta	500cc
1965	Yamaha	250cc
1965	Suzuki	125cc
1965	Honda	350cc
1965	Honda	50cc
1964	MV Agusta	500cc
1964	Yamaha	250cc
1964	Honda	125cc
1964	Honda	350cc
1964	Suzuki	50cc
1963	MV Agusta	500cc
1963	Honda	250cc
1963	Suzuki	125cc
1963	Honda	350cc
1963	Suzuki	50cc
1962	MV Agusta	500cc
1962	Honda	250cc
1962	Honda	125cc
1962	Honda	350cc
1962	Suzuki	50cc
1961	MV Agusta	500cc
1961	Honda	250cc
1961	Honda	125cc
1961	MV Agusta	350cc
1960	MV Agusta	Mot500ccoGP™
1960	MV Agusta	250cc
1960	MV Agusta	125cc
1960	MV Agusta	350cc
1959	MV Agusta	500cc
1959	MV Agusta	250cc
1959	MV Agusta	125cc
1959	MV Agusta	350cc
1958	MV Agusta	500cc
1958	MV Agusta	250cc
1958	MV Agusta	125cc
1958	MV Agusta	350cc
1957	Gilera	500cc
1957	Mondial	250cc
1957	Mondial	125cc
1957	Moto Guzzi	350cc
1956	MV Agusta	Moto500ccGP™
1956	MV Agusta	250cc
1956	MV Agusta	125cc
1956	Moto Guzzi	350cc
1955	Gilera	500cc
1955	NSU	250cc
1955	MV Agusta	125cc
1955	Moto Guzzi	350cc
1954	Gilera	500cc
1954	NSU	250cc
1954	NSU	125cc
1954	Moto Guzzi	350cc
1953	Gilera	500cc
1953	NSU	250cc
1953	NSU	125cc
1953	Moto Guzzi	350cc
1952	Gilera	500cc
1952	Moto Guzzi	250cc
1952	MV Agusta	125cc
1952	Norton	350cc
1951	Norton	500cc
1951	Moto Guzzi	250cc
1951	Mondial	125cc
1951	Norton	350cc
1950	Gilera	500cc
1950	Benelli	250cc
1950	Mondial	125cc
1950	Velocette	350cc
1949	AJS	500cc
1949	Moto Guzzi	250cc
1949	Mondial	125cc
1949	Velocette	350cc
"""

winners_data_IO = StringIO(winners_data)
winners = pd.read_csv(winners_data_IO, sep = '\t')

winners.head()

print(winners.shape)

print(winners.columns)

winners.info()

"""#Descobrindo todas as categorias e suas ocorrências"""

categories = winners.groupby('Class').count()
categories.drop('Constructor', axis = 1, inplace= True)
categories.sort_values(by = 'Season', ascending=False, inplace = True)
categories.reset_index(inplace = True)
categories.rename(columns = {'Season': 'Seasons'}, inplace = True)

categories

paleta = sns.color_palette("flare", 12)
sns.set_style("whitegrid")
plt.figure(figsize = (15,5))
h = sns.catplot(data = categories, x = 'Class', y = 'Seasons', kind = 'bar',
                palette = paleta, aspect = 2)
h.set_xticklabels(rotation = 45)
plt.show

df = winners.groupby(['Class', 'Constructor',]).count()
df

"""#Descobrindo todos os vencedores e sua ocorrência"""

total_wins= winners.groupby('Constructor').count()
total_wins.drop('Class', axis = 1, inplace= True)
total_wins.sort_values(by = 'Season', ascending=False, inplace = True)
total_wins.reset_index(inplace = True)
total_wins.rename(columns = {'Season': 'Victories'}, inplace = True)

total_wins

paleta = sns.color_palette('rocket', 40)
sns.set_style("whitegrid")
plt.figure(figsize = (20,6))
h = sns.catplot(data = total_wins, x = 'Constructor', y = 'Victories', kind = 'bar',
                palette = paleta, aspect = 2)
h.set_xticklabels(rotation = 90)
plt.show

total_wins.describe()

fig = px.box(total_wins, x = 'Victories')
fig.show()

"""#outsiders Honda Yamaha MV Agusta
#agora, vamos agrupar esses 3 vencedores através das categorias
"""

outsiders = ['Honda', 'Yamaha', 'MV Agusta']
winners_outsiders = winners.query('Constructor in @outsiders').groupby(['Season', 'Constructor']).count().reset_index()
winners_outsiders

h = sns.catplot(data = winners_outsiders, x = 'Season', y = 'Class', hue = 'Constructor', kind = 'bar',aspect = 3)
h.set_xticklabels(rotation = 90)

winners.query("Constructor == 'Honda'").groupby('Class')['Constructor'].count()

winners.query("Constructor == 'Yamaha'").groupby('Class')['Constructor'].count()

winners.query("Constructor == 'MV Agusta'").groupby('Class')['Constructor'].count()

df = winners.query('Constructor in @outsiders').groupby(['Constructor', 'Class']).count()
df.reset_index(inplace = True)
df.rename(columns = {'Season': 'Victories'}, inplace = True)
df

fig = px.scatter(df, x = 'Class', y = 'Constructor', size = 'Victories', color = 'Victories')
fig.show()

fig = px.density_heatmap(df, x = 'Class', z = 'Victories', y = 'Constructor')
fig.show()

Honda = winners_outsiders.query('Constructor == "Honda"')
Honda.reset_index(inplace = True)
Honda.drop(['index', 'Constructor'], axis = 1, inplace = True)
Honda.rename(columns = {'Class': 'Victories'}, inplace = True)

Honda.head()

Y = Honda.Victories
X = sm.add_constant(Honda.Season)
regression_result = sm.OLS(Y, X, missing = 'drop').fit()

print(f'A quantidade de títulos conquistados pela Honda em 2023 será de : {regression_result.predict([1, 2023])[0]:.2f}')
print(f'A quantidade de títulos conquistados pela Honda em 2024 será de : {regression_result.predict([1, 2024])[0]:.2f}')
print(f'A quantidade de títulos conquistados pela Honda em 2025 será de : {regression_result.predict([1, 2025])[0]:.2f}')
print(f'A quantidade de títulos conquistados pela Honda em 2026 será de : {regression_result.predict([1, 2026])[0]:.2f}')
print(f'A quantidade de títulos conquistados pela Honda em 2027 será de : {regression_result.predict([1, 2027])[0]:.2f}')
print(f'A quantidade de títulos conquistados pela Honda em 2028 será de : {regression_result.predict([1, 2028])[0]:.2f}')
print(f'A quantidade de títulos conquistados pela Honda em 2029 será de : {regression_result.predict([1, 2029])[0]:.2f}')
print(f'A quantidade de títulos conquistados pela Honda em 2030 será de : {regression_result.predict([1, 2030])[0]:.2f}')

R2 = regression_result.rsquared
R2

"""#YAMAHA"""

Yamaha = winners_outsiders.query('Constructor == "Yamaha"')
Yamaha.reset_index(inplace = True)
Yamaha.drop(['index', 'Constructor'], axis = 1, inplace = True)
Yamaha.rename(columns = {'Class': 'Victories'}, inplace = True)

Y = Yamaha.Victories
X = sm.add_constant(Yamaha.Season)
regression_result = sm.OLS(Y, X, missing = 'drop').fit()

print(f'A quantidade de títulos conquistados pela Yamaha em 2023 será de : {regression_result.predict([1, 2023])[0]:.2f}')
print(f'A quantidade de títulos conquistados pela Yamaha em 2024 será de : {regression_result.predict([1, 2024])[0]:.2f}')
print(f'A quantidade de títulos conquistados pela Yamaha em 2025 será de : {regression_result.predict([1, 2025])[0]:.2f}')
print(f'A quantidade de títulos conquistados pela Yamaha em 2026 será de : {regression_result.predict([1, 2026])[0]:.2f}')
print(f'A quantidade de títulos conquistados pela Yamaha em 2027 será de : {regression_result.predict([1, 2027])[0]:.2f}')
print(f'A quantidade de títulos conquistados pela Yamaha em 2028 será de : {regression_result.predict([1, 2028])[0]:.2f}')
print(f'A quantidade de títulos conquistados pela Yamaha em 2029 será de : {regression_result.predict([1, 2029])[0]:.2f}')
print(f'A quantidade de títulos conquistados pela Yamaha em 2030 será de : {regression_result.predict([1, 2030])[0]:.2f}')

R2 = regression_result.rsquared
R2

"""#MV Agusta"""

MV_Agusta = winners_outsiders.query('Constructor == "MV Agusta"')
MV_Agusta.reset_index(inplace = True)
MV_Agusta.drop(['index', 'Constructor'], axis = 1, inplace = True)
MV_Agusta.rename(columns = {'Class': 'Victories'}, inplace = True)

Y = MV_Agusta.Victories
X = sm.add_constant(MV_Agusta.Season)
regression_result = sm.OLS(Y, X, missing = 'drop').fit()

print(f'A quantidade de títulos conquistados pela MV Agusta em 2023 será de : {regression_result.predict([1, 2023])[0]:.2f}')
print(f'A quantidade de títulos conquistados pela MV Agusta em 2024 será de : {regression_result.predict([1, 2024])[0]:.2f}')
print(f'A quantidade de títulos conquistados pela MV Agusta em 2025 será de : {regression_result.predict([1, 2025])[0]:.2f}')
print(f'A quantidade de títulos conquistados pela MV Agusta em 2026 será de : {regression_result.predict([1, 2026])[0]:.2f}')
print(f'A quantidade de títulos conquistados pela MV Agusta em 2027 será de : {regression_result.predict([1, 2027])[0]:.2f}')
print(f'A quantidade de títulos conquistados pela MV Agusta em 2028 será de : {regression_result.predict([1, 2028])[0]:.2f}')
print(f'A quantidade de títulos conquistados pela MV Agusta em 2029 será de : {regression_result.predict([1, 2029])[0]:.2f}')
print(f'A quantidade de títulos conquistados pela MV Agusta em 2030 será de : {regression_result.predict([1, 2030])[0]:.2f}')

R2 = regression_result.rsquared
R2

