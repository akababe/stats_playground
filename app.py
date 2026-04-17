import gradio as gr
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statslab import visualizing_data, analyzing_data, data_distributions, sampling_inference, regression_chi_square, discrete_random_variables

# Set default style for plots
plt.style.use('bmh')

def get_plot_from_plt():
    """Captures the current matplotlib figure."""
    fig = plt.gcf()
    return fig

# --- Module 1 & 2: Data Exploration ---
def analyze_data_explorer(data_str):
    try:
        data = [float(x.strip()) for x in data_str.split(',')]
        summary = analyzing_data.full_univariate_summary(data)
        
        # Create text summary
        text_res = f"### Summary Statistics\n"
        text_res += f"- **Mean:** {summary['mean']:.4f}\n"
        text_res += f"- **Median:** {summary['median']:.4f}\n"
        text_res += f"- **Std Dev:** {summary['std_dev']:.4f}\n"
        text_res += f"- **IQR:** {summary['iqr']:.4f}\n"
        text_res += f"- **Outliers:** {summary['outliers']}\n"
        
        # Create plots
        plt.figure(figsize=(12, 5))
        
        plt.subplot(1, 2, 1)
        visualizing_data.plot_histogram(data, title="Distribution")
        
        plt.subplot(1, 2, 2)
        analyzing_data.plot_box_plot(data, title="Box Plot")
        
        plt.tight_layout()
        return text_res, get_plot_from_plt()
    except Exception as e:
        return f"Error: {e}", None

# --- Module 3: Distributions ---
def distribution_explorer(data_str):
    try:
        data = [float(x.strip()) for x in data_str.split(',')]
        shape = data_distributions.shape_measures(data)
        normality = data_distributions.is_normal_ish(data)
        
        text_res = f"### Distribution Shape\n"
        text_res += f"- **Skewness:** {shape['skewness']:.4f}\n"
        text_res += f"- **Kurtosis:** {shape['kurtosis']:.4f}\n"
        text_res += f"- **Normal? (Shapiro):** {'Yes' if normality['is_normal'] else 'No'} (p={normality['shapiro_p_value']:.4f})\n"
        
        plt.figure(figsize=(8, 5))
        data_distributions.plot_histogram_with_density(data)
        
        return text_res, get_plot_from_plt()
    except Exception as e:
        return f"Error: {e}", None

# --- Module 6: CLT Simulator ---
def clt_simulator_demo(dist_type, sample_size, num_samples):
    if dist_type == "Uniform":
        pop = np.random.uniform(0, 100, 10000)
    elif dist_type == "Exponential":
        pop = np.random.exponential(10, 10000)
    else: # Normal
        pop = np.random.normal(50, 15, 10000)
        
    plt.figure(figsize=(10, 6))
    sampling_inference.simulate_clt(pop, sample_size=int(sample_size), num_samples=int(num_samples))
    return get_plot_from_plt()

# --- Module 8: Regression ---
def regression_explorer(x_str, y_str):
    try:
        x = [float(i.strip()) for i in x_str.split(',')]
        y = [float(i.strip()) for i in y_str.split(',')]
        
        res = regression_chi_square.linear_regression(x, y)
        
        text_res = f"### Regression Results\n"
        text_res += f"- **Equation:** y = {res['intercept']:.4f} + {res['slope']:.4f}x\n"
        text_res += f"- **R-squared:** {res['r_squared']:.4f}\n"
        text_res += f"- **Correlation (r):** {res['r_value']:.4f}\n"
        text_res += f"- **P-value:** {res['p_value']:.4f}\n"
        
        plt.figure(figsize=(12, 5))
        plt.subplot(1, 2, 1)
        regression_chi_square.plot_regression_line(x, y)
        
        plt.subplot(1, 2, 2)
        regression_chi_square.plot_residuals(x, res['residuals'])
        
        plt.tight_layout()
        return text_res, get_plot_from_plt()
    except Exception as e:
        return f"Error: {e}", None

# --- Gradio UI Layout ---
with gr.Blocks(title="Python StatsLab Playground") as demo:
    gr.Markdown("# 📊 Python StatsLab Playground")
    gr.Markdown("An interactive educational environment for exploring statistical concepts.")
    
    with gr.Tabs():
        with gr.TabItem("1. Univariate Analysis"):
            gr.Markdown("### Descriptive Statistics & Visuals")
            data_input = gr.Textbox(label="Data (comma separated)", value="10, 12, 12, 13, 12, 11, 14, 13, 15, 10, 10, 10, 25")
            btn_analyze = gr.Button("Run Analysis")
            with gr.Row():
                text_out = gr.Markdown()
                plot_out = gr.Plot()
            btn_analyze.click(analyze_data_explorer, inputs=data_input, outputs=[text_out, plot_out])
            
        with gr.TabItem("2. Distributions"):
            gr.Markdown("### Skewness, Kurtosis & Normality")
            dist_input = gr.Textbox(label="Data (comma separated)", value="1, 2, 2, 3, 3, 3, 4, 4, 5")
            btn_dist = gr.Button("Check Distribution")
            with gr.Row():
                dist_text = gr.Markdown()
                dist_plot = gr.Plot()
            btn_dist.click(distribution_explorer, inputs=dist_input, outputs=[dist_text, dist_plot])

        with gr.TabItem("3. CLT Simulator"):
            gr.Markdown("### Central Limit Theorem")
            with gr.Row():
                dist_type = gr.Dropdown(["Normal", "Uniform", "Exponential"], label="Population Distribution", value="Uniform")
                n_size = gr.Slider(5, 100, step=5, label="Sample Size (n)", value=30)
                n_samples = gr.Slider(100, 5000, step=100, label="Number of Samples", value=1000)
            btn_clt = gr.Button("Simulate")
            clt_plot = gr.Plot()
            btn_clt.click(clt_simulator_demo, inputs=[dist_type, n_size, n_samples], outputs=clt_plot)

        with gr.TabItem("4. Regression"):
            gr.Markdown("### Linear Regression & Correlation")
            with gr.Row():
                x_in = gr.Textbox(label="X Variable (comma separated)", value="1, 2, 3, 4, 5, 6, 7, 8")
                y_in = gr.Textbox(label="Y Variable (comma separated)", value="2.1, 3.9, 6.2, 8.1, 10.1, 12.2, 13.9, 16.1")
            btn_reg = gr.Button("Run Regression")
            with gr.Row():
                reg_text = gr.Markdown()
                reg_plot = gr.Plot()
            btn_reg.click(regression_explorer, inputs=[x_in, y_in], outputs=[reg_text, reg_plot])

if __name__ == "__main__":
    demo.launch()
