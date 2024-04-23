import pandas as pd
from scipy import stats

# File paths for combined data files
city_national_combined_file_path = r"C:\Users\91901\Downloads\CityNationalBank_combined.csv"
park_national_combined_file_path = r"C:\Users\91901\Downloads\ParkNationalBank_combined.csv"
city_national_2017_file_path = r"C:\Users\91901\Downloads\CityNationalBank_2017.csv"  # Replace with actual file path
park_national_2017_file_path = r"C:\Users\91901\Downloads\ParkNationalBank_2017.csv"  # Replace with actual file path

# Load combined data for City National Bank and Park National Bank
city_national_data = pd.read_csv(city_national_combined_file_path)
park_national_data = pd.read_csv(park_national_combined_file_path)

# Load 2017 data for City National Bank and Park National Bank
city_national_data_2017 = pd.read_csv(city_national_2017_file_path)
park_national_data_2017 = pd.read_csv(park_national_2017_file_path)

# Merge 2017 data with the combined data
city_national_data = pd.concat([city_national_data, city_national_data_2017])
park_national_data = pd.concat([park_national_data, park_national_data_2017])

# Define the banks involved in redlining cases
redlining_banks = {
    'City National Bank': '593C3GZG957YOJPS2Z63',
    'Park National Bank': '549300CEHN5CVC6INV48'
}

# Define the criteria for selecting peers (e.g., same geographic area, similar size, etc.)
# For demonstration purposes, let's assume peers are banks in the same state
peers = {
    'City National Bank': 'CA',
    'Park National Bank': 'OH'
}

# Perform analysis for each bank involved in redlining cases
for bank, lei in redlining_banks.items():
    if bank == 'City National Bank':
        bank_data = city_national_data[city_national_data['respondent_id'] == lei]  # Filter data for the bank
    elif bank == 'Park National Bank':
        bank_data = park_national_data[park_national_data['respondent_id'] == lei]  # Filter data for the bank

    peer_data = city_national_data[city_national_data['state_abbr'] == peers[bank]]  # Filter data for peers (assuming peers are in the same state as City National Bank)
    
    # Calculate statistical measures for comparison (e.g., mean loan amount)
    bank_means = bank_data.groupby('year')['loan_amount_000s'].mean()
    peer_means = peer_data.groupby('year')['loan_amount_000s'].mean()

    # Perform statistical tests (e.g., t-test) to determine if there are significant differences between the bank and its peers
    t_stat, p_value = stats.ttest_ind(bank_means, peer_means)

    # Additional statistical analysis
    bank_loan_count = bank_data.groupby('year')['loan_amount_000s'].count()
    peer_loan_count = peer_data.groupby('year')['loan_amount_000s'].count()
    loan_count_diff = bank_loan_count - peer_loan_count

    # Output the results
    print(f"Results for {bank}:")
    print(f"Mean Loan Amounts - {bank}:")
    print(bank_means)
    print(f"Mean Loan Amounts - Peers:")
    print(peer_means)
    print(f"Statistical Test (t-statistic, p-value): ({t_stat}, {p_value})")
    print(f"Loan Count Difference - {bank}:")
    print(loan_count_diff)
    print()

    # Additional statistical analysis or visualizations can be added here
import pandas as pd
import matplotlib.pyplot as plt

# File paths for combined data files
city_national_combined_file_path = r"C:\Users\91901\Downloads\CityNationalBank_combined.csv"
park_national_combined_file_path = r"C:\Users\91901\Downloads\ParkNationalBank_combined.csv"
city_national_2017_file_path = r"C:\Users\91901\Downloads\CityNationalBank_2017.csv"  # Replace with actual file path
park_national_2017_file_path = r"C:\Users\91901\Downloads\ParkNationalBank_2017.csv"  # Replace with actual file path

# Load combined data for City National Bank and Park National Bank
city_national_data = pd.read_csv(city_national_combined_file_path)
park_national_data = pd.read_csv(park_national_combined_file_path)

# Load 2017 data for City National Bank and Park National Bank
city_national_data_2017 = pd.read_csv(city_national_2017_file_path)
park_national_data_2017 = pd.read_csv(park_national_2017_file_path)

# Merge 2017 data with the combined data
city_national_data = pd.concat([city_national_data, city_national_data_2017])
park_national_data = pd.concat([park_national_data, park_national_data_2017])

# Define the banks involved in redlining cases
redlining_banks = {
    'City National Bank': '593C3GZG957YOJPS2Z63',
    'Park National Bank': '549300CEHN5CVC6INV48'
}

# Define the criteria for selecting peers (e.g., same geographic area, similar size, etc.)
# For demonstration purposes, let's assume peers are banks in the same state
peers = {
    'City National Bank': 'CA',
    'Park National Bank': 'OH'
}

# Perform analysis for each bank involved in redlining cases
for bank, lei in redlining_banks.items():
    if bank == 'City National Bank':
        bank_data = city_national_data[city_national_data['respondent_id'] == lei]  # Filter data for the bank
    elif bank == 'Park National Bank':
        bank_data = park_national_data[park_national_data['respondent_id'] == lei]  # Filter data for the bank

    peer_data = city_national_data[city_national_data['state_abbr'] == peers[bank]]  # Filter data for peers (assuming peers are in the same state as City National Bank)
    
    # Calculate statistical measures for comparison (e.g., mean loan amount)
    bank_means = bank_data.groupby('year')['loan_amount_000s'].mean()
    peer_means = peer_data.groupby('year')['loan_amount_000s'].mean()

    # Perform statistical tests (e.g., t-test) to determine if there are significant differences between the bank and its peers
    t_stat, p_value = stats.ttest_ind(bank_means, peer_means)

    # Additional statistical analysis
    bank_loan_count = bank_data.groupby('year')['loan_amount_000s'].count()
    peer_loan_count = peer_data.groupby('year')['loan_amount_000s'].count()
    loan_count_diff = bank_loan_count - peer_loan_count

    # Output the results
    print(f"Results for {bank}:")
    print(f"Mean Loan Amounts - {bank}:")
    print(bank_means)
    print(f"Mean Loan Amounts - Peers:")
    print(peer_means)
    print(f"Statistical Test (t-statistic, p-value): ({t_stat}, {p_value})")
    print(f"Loan Count Difference - {bank}:")
    print(loan_count_diff)
    print()

    # Time series plot for loan approval rates
    fig, ax = plt.subplots()
    ax.plot(bank_means.index, bank_means.values, label=f'{bank}')
    ax.plot(peer_means.index, peer_means.values, label='Peers')
    ax.set_xlabel('Year')
    ax.set_ylabel('Mean Loan Amount')
    ax.set_title(f'Mean Loan Amount Over Time for {bank} and Peers')
    ax.legend()
    plt.show()
