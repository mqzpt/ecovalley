# EcoValley

## Inspiration

As sustainability becomes a critical aspect of modern projects, we were inspired to create a tool that helps users make informed decisions about the materials they use. We recognized that many sustainability tools are geared toward large corporations with significant resources, leaving smaller businesses and individuals with fewer options. EcoValley was created to bridge this gap, making eco-conscious material selection accessible to everyone. Our goal is to empower individuals and small businesses to reduce their environmental impact just as effectively as larger companies, without the need for costly, complex software.

## What it does

EcoValley takes a user’s natural language input, such as describing the type of product they are looking to create, and uses the Cohere LLM API to suggest three lists of material options. Each list includes the materials best suited for the project, along with the amount required in kilograms.

Once the material options are generated, EcoValley performs further calculations using data from our custom research. We built a CSV file that includes essential metrics for each material, such as energy used in production, carbon emissions, water use, and cost per kilogram. Using this data, EcoValley calculates the overall environmental impact and financial costs of the selected materials, giving users a complete breakdown to make the most sustainable choice.

## How we built it

We developed EcoValley using a combination of full-stack web development tools. The front-end was built with Flask for a clean, user-friendly interface, while the back-end integrates the Cohere LLM API for material selection. The LLM takes user inputs, interprets their needs, and returns structured data in the form of materials and their required quantities.

Once we have the materials, we use our research-backed data to calculate the energy used, carbon emissions produced, water consumption, and cost, mostly with Pandas. This data allows us to present users with an easy-to-compare analysis for each set of materials.

## Challenges we ran into

One of the main challenges was ensuring that the output from the Cohere LLM API was structured in a way that could be processed programmatically. Initially, it was difficult to get well-structured data from the LLM, as it required fine-tuning to return material options in a consistent format that we could use for calculations. This involved multiple iterations on the prompt and testing various temperature settings to improve the quality and consistency of the results.

Another challenge was compiling accurate and reliable data for our materials CSV file. We conducted extensive research to ensure that the values for energy use, carbon emissions, water use, and cost were accurate and up-to-date for each material.

## Accomplishments that we're proud of

We’re proud of how EcoValley makes sustainable material selection accessible to average users and small businesses, not just large corporations with the resources to afford expensive software like Ansys EcoAudit. By integrating the Cohere LLM API and our custom materials database, we’ve built a tool that simplifies complex material sourcing decisions, offering eco-friendly options to anyone looking to reduce their environmental footprint. Our platform empowers individuals and small businesses to make informed, sustainable choices without needing high-cost, industry-specific software.

## What we learned

This project taught us how to leverage AI-powered language models to create tangible, impactful tools. We gained insights into handling unstructured outputs from LLMs and converting them into usable formats for further analysis. Additionally, we learned the importance of thorough research in creating a reliable database that supports accurate calculations.

## What's next for EcoValley

Moving forward, we plan to expand the material database and offer more detailed comparisons, including factors like lifecycle analysis and recyclability. We also aim to collaborate with material suppliers, allowing users to purchase sustainable materials directly through the platform. Another goal is to enhance our AI’s understanding of user input, making it even more intuitive and user-friendly.
