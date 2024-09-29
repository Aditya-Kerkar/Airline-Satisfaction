



import pandas as pd


df = pd.read_csv('original.csv')


threshold = 3.5


df['satisfaction'] = df[['Inflight wifi service', 'Departure/Arrival time convenient', 'Ease of Online booking','Gate location',
                          'Food and drink','Online boarding','Seat comfort','Inflight entertainment','On-board service','Leg room service'
                          ,'Baggage handling','Checkin service','Inflight service',
                         'Cleanliness']].mean(axis=1).apply(lambda x: 'satisfied' if x >= threshold else 'neutral or dissatisfied')


df.to_csv('train.csv', index=False)

