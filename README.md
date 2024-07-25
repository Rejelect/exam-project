# Xodimlar Ma'lumotlari Dashboard

This Streamlit project provides an interactive dashboard for analyzing employee data. The dashboard includes features for viewing data descriptions, handling null values, and generating various visualizations such as count plots, histograms, line plots, box plots, and heatmaps.

## Features

- **Data Overview**: Detailed descriptions of each column and summary statistics of the dataset.
- **Null Values Handling**: Options to fill or remove null values using various methods such as mode, median, and mean.
- **Visualizations**: A variety of plots to explore and analyze the dataset, including:
  - Count plots for gender distribution, work-life balance vs job satisfaction.
  - Histograms and line plots for age distribution and its effect on monthly income.
  - Box plots for monthly income vs job satisfaction and marital status vs job satisfaction.
  - Heatmaps for correlation analysis between numerical columns.
  - Violin plots for the distribution of monthly income across job levels.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/employee-dashboard.git
   ```
2. Change to the project directory:
   ```sh
   cd employee-dashboard
   ```
3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Place your dataset (`22.csv`) in the project directory.
2. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```
3. Open your web browser and go to `http://localhost:8501` to access the dashboard.

## Dataset

The project uses an employee dataset (`22.csv`) which contains the following columns:

- **Unnamed: 0**: Index or identifier for each row.
- **Employee ID**: Unique identifier for each employee.
- **Age**: Age of the employee.
- **Gender**: Gender of the employee.
- **Years at Company**: Number of years the employee has worked at the company.
- **Job Role**: The role or position of the employee in the company.
- **Monthly Income**: Monthly income of the employee.
- **Work-Life Balance**: Employee's rating of their work-life balance.
- **Job Satisfaction**: Employee's level of job satisfaction.
- **Performance Rating**: Employee's performance rating.
- **Number of Promotions**: Number of promotions the employee has received.
- **Overtime**: Indicates if the employee works overtime.
- **Distance from Home**: Distance between the employee's home and workplace.
- **Education Level**: The highest education level attained by the employee.
- **Marital Status**: Marital status of the employee.
- **Number of Dependents**: Number of dependents the employee has.
- **Job Level**: Job level or rank within the company.
- **Company Size**: Size of the company.
- **Company Tenure**: Employee's tenure at the company.
- **Remote Work**: Indicates if the employee works remotely.
- **Leadership Opportunities**: Opportunities for leadership roles.
- **Innovation Opportunities**: Opportunities for innovative projects or tasks.
- **Company Reputation**: Employee's perception of the company's reputation.
- **Employee Recognition**: Recognition of the employee's achievements at work.
- **Attrition**: Indicates if the employee has left the company.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

