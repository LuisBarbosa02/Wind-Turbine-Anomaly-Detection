# Import libraries
from .data_generator import SensorDataGenerator
import pandas as pd
from ..config import DATA_FOLDER

# Create data
if __name__ == '__main__':
    gen = SensorDataGenerator()
    df = pd.DataFrame(
        columns=['timestamp', 'temperature', 'humidity', 'sound', 'anomaly']
    )

    n_samples = int(input('Insert number of samples: '))
    for _ in range(n_samples):
        data = gen.step()
        df.loc[len(df)] = data

    print(df, '\n')

    file_name = input('Insert file name without the extension (default is testing_data): ')
    file_name = 'testing_data' if file_name == '' else file_name
    df.to_csv(f'{DATA_FOLDER}/{file_name}.csv', index=False)