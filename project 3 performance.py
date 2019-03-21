import pandas as pd
from sqlalchemy import create_engine


driver = 'mysql+pymysql:'
user = 'root'
password = 'paugasol'
ip = '35.246.57.187'
database = 'NBA'
connection_string = f'{driver}//{user}:{password}@{ip}/{database}'
engine = create_engine(connection_string)
query = 'SELECT * FROM performance'
performance = pd.read_sql(query, engine)


%md
PTS Points
REB Rebounds 
AST Assists
PIE Player Impact Estimate


performance[['pts','ast','reb','pie']].describe()


%sql
SELECT * FROM performance ORDER BY pie DESC

%sql
SELECT * FROM performance ORDER BY pts DESC

%sql
SELECT * FROM performance ORDER BY ast DESC

%sql
SELECT * FROM performance ORDER BY reb DESC

corr = performance.corr()
corr


%md
highest positive correlation between assist and points (0.683074)
also high positive corr. between rebounds and points (0.665074)
Formula (PTS + FGM + FTM - FGA - FTA + DREB + (.5 * OREB) + AST + STL + (.5 * BLK) - PF - TO) / (GmPTS + GmFGM + GmFTM - GmFGA - GmFTA + GmDREB + (.5 * GmOREB) + GmAST + GmSTL + (.5 * GmBLK) - GmPF - GmTO)
What you do (season) / what happens in the game
What you do = x + 1*PTS + 1.5*RBS + 1*AST --> Weight of RBS on PIE >> weight PTS ans AST -->OK BUT according to the formula we should weight of PTS = weight of AST HOWEVER we can see that corr(AST vs. PIE) = 0.4 and coor(PTS vs. PIE)=0.57 --> Hence PTS affect more positively than assists to the game outcome