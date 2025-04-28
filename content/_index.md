---
# Leave the homepage title empty to use the site title
title: ''
date: 2022-10-24
type: landing

sections:

  - block: about.biography
    id: about
    content:
      title: About me
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: admin

  # - block: skills
  #   content:
  #     title: Skills
  #     text: 'I develop end-to-end AI solutions' 
      
  #     # Choose a user to display skills from (a folder name within `content/authors/`)
  #     username: admin
  #   design:
  #     columns: '1'
  
  - block: experience
    content:
      title: Current experience
      items:
        ## -- UW -- ##
        - title: Postdoctoral Data Scientist
          company: UW-Madison - Top 15 public universities in the US
          company_url: 'https://gibbs-lab.wisc.edu/caina-max-couto-silva.html'
          company_logo: uw-madison
          location: Madison - WI, USA
          date_start: '2024-08-01'
          date_end: ''
          description: |1-

              - Currently developing a RAG-based **text-to-SQL AI** agent that allows users to interact with the database using Slack.
              - Developed **[SQLDeps](https://sqldeps.readthedocs.io/)**: an **open-source Python package leveraging LLMs** to automatically extract table and column dependencies and outputs from complex SQL scripts **100X faster and >300X cheaper** than human expert labor.
              - Developed and optimized **cattle mapping** using cutting-edge deep learning models on high‑resolution satellite imagery, providing actionable intelligence to combat Amazon deforestation.
              - Engineered a pioneering **machine learning classifier** to assess data quality from farm properties at scale, implementing feature engineering on geospatial and entity data that enabled scalable data integrity checks for the first time.
              - **Lead UW‑Madison students** in research projects, mentoring on machine learning and computer vision techniques.
              - **Automated database workflows**, reducing manual intervention and boosting team productivity.
              - Delivered private **data analysis reports** for stakeholders in Brazil and the USA.
              
              **Tools:** Python, SQL, GitHub/GitLab, git, AWS, LangChain, PyTorch, YOLO, LLMs, Streamlit, machine learning libraries (e.g., scikit-learn), data visualization libraries, etc.

    design:
      columns: '2'

  - block: experience
    content:
      title: Industry experience
      # Date format for experience
      #   Refer to https://docs.hugoblox.com/customization/#date-format
      date_format: Jan 2006
      # Experiences.
      #   Add/remove as many `experience` items below as you like.
      #   Required fields are `title`, `company`, and `date_start`.
      #   Leave `date_end` empty if it's your current employer.
      #   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
      
      items:
        ## -- SLB -- ##
        - title: Data Scientist
          company: Schlumberger - World's largest offshore drilling company
          company_url: ''
          company_logo: slb
          location: Houston - TX, USA (remote)
          date_start: '2023-01-01'
          date_end: '2024-07-31'
          description: |1-
              I work developing end-to-end AI SaaS products to our internal customers.

              **Main activities:**  
              - Building predictive models using either statistical or machine learning approaches to assess the health of the company assets (tools)
              - Assessing the technical feasibility of new projects through data analysis
              
              **Deliveries:**
              - Statistical models to assess the asset health
              - Machine learning models to predict the asset health for the upcoming usage
              - A custom-trained OCR model to extract dimensions of engineering drawings
              
              **Quick facts:**
              - As result of my first project, our work has been accepted to be published as a scientific paper at OnePetro.
              - I led a innovation proposal using AI, and we ranked in the top 12 out of almost 400 ideas worldwide. My colleague and I gave the final pitch to the CEOs.
              - I work in one of the most diverse teams in our company, interacting with people from US, India, Europe, and South America in my daily routine.
              
              &nbsp;
              
              **Tools:** Dataiku, GCP, SQL, Python, Dash, Streamlit, machine learning libraries (e.g., scikit-learn), data visualization libraries.
        
        ## -- DNC -- ##
        - title: Data Science Consultor (Education)
          company: DNC  - Edtech
          company_url: ''
          company_logo: escola-dnc
          location: São Paulo - SP, Brazil (remote)
          date_start: '2021-10-01'
          date_end: '2024-07-31'
          description: |1-
            I have worked in multiple roles: facilitator, mentor, and consultant/instructor.
  
            As a consultant/instructor, I prepared the course modules and recorded classes. I recorded four modules: statistics, data cleaning/wrangling, clustering, and model deployment. I have also devised data science activities about descriptive and inferential statistics, unsupervised machine learning models, MLFlow, big data with PySpark, among others. 
            
            As a mentor, I assessed student reports and addressed their questions through Q&A sessions, aiding in academic and real-world projects.
            
            As a facilitator, I participated in data science activities from exploratory analysis to model deployment. I also prepared some of those activities.
        
        ## -- Ambev Tech -- ##
        - title: Data Scientist
          company: Ambev Tech  - World's largest beer brewer company
          company_url: ''
          company_logo: ab-inbev
          location: São Paulo - SP, Brazil (remote)
          date_start: '2022-05-01'
          date_end: '2022-12-31'
          description: |2-
            Squad: Revenue Management

            **Activities / Deliverables:**
            - Rule-based automation of pipelines for price engines using PySpark (big data)
            - Statistical model to identify price changepoints for several SKU categories
            - Monthly time series modeling from of selling volume using state-of-the-art forecast and hierarchical reconciliation methods
            - Training for data scientists

            &nbsp;

            **Tools:** • Python • PySpark • MLFlow • Scikit-learn • Pycaret • Statsmodels • Forecasting frameworks (Prophet, NeuralProphet, StatsForecast)
            
        ## -- Remessa Online -- ##
        - title: Data Scientist
          company: Remessa Online  - Fintech
          company_url: ''
          company_logo: remessa-online
          location: São Paulo - SP, Brazil (remote)
          date_start: '2021-10-01'
          date_end: '2022-04-01'
          description: |1-
            **Activities:**  
            - Advanced statistical modeling: data exploratory analysis, hypothesis testing, time series forecasting, predictive analyses (e.g., regression and classification), customer and product segmentation, etc.
            
            **Deliverables:**  
            - Multiple time series forecasting for customer segments (weekly and monthly)
            - Model for predicting the probability of the customer recurrence
            - In-depth study of churn analysis through inferential statistics

            &nbsp;
            
            **Tools:** • Python • PySpark • MLFlow • Scikit-learn • Pycaret • Catboost • Prophet • AWS • GitHub • Data visualization libraries (Plotly, Seaborn, Matplotlib)
            
        ## -- Eli Lilly -- ##
        - title: Safety Data Sciences Associate
          company: Eli Lilly
          company_url: ''
          company_logo: eli-lilly
          location: Indianopolis - IN, USA (remote)
          date_start: '2021-06-01'
          date_end: '2021-10-01'
          description: |2-
            **Activities:**  
            - Queries and reports for worldwide company members

    design:
      columns: '2'


  - block: experience
    content:
      title: Academic experience
      items:
      
        ## -- MBA -- ##
        - title: MBA in Data Science & Analytics
          company: Universidade de São Paulo
          company_url: ''
          company_logo: usp
          location: São Paulo - SP, Brazil
          date_start: '2021-05-01'
          date_end: '2023-08-01'
          description: |1-
            
            Grade: 10
            
            - In‑depth study of machine learning models.
            - Developed an end‑to‑end hybrid ML model for churn prediction.
            - [Project code repository](https://github.com/cmcouto-silva/telco-churn)
            
      
        ## -- PhD -- ##
        - title: PhD Researcher
          company: Universidade de São Paulo
          company_url: ''
          company_logo: usp
          location: São Paulo - SP, Brazil
          date_start: '2016-07-01'
          date_end: '2021-04-01'
          description: |1-
            
            Thesis: Identifying natural selection in Native American populations.
            Supported by: CAPES (2016 - 2018) and FAPESP (2018 - 2020)
            
            **Activities:**  
            - Data analysis, visualization, and scientific reporting of genetic data using R, Python, and bash scripting.
            - Application of non‑supervised algorithms (e.g., PCA), descriptive and inferential statistics.
            
            **Deliverables:**  
            - Internal R package with customized functions to facilitate multiple analyses
            - Three scientific papers published in international magazines
            - [Thesis code repository](https://github.com/cmcouto-silva/tese)  
            &nbsp;
            
            I presented our preliminar work in international conferences, including USA. I also took a internship of 3 months in Barcelona - Spain.

        ## -- MSc -- ##
        - title: Master in Science
          company: Universidade de São Paulo
          company_url: ''
          company_logo: usp
          location: São Paulo - SP, Brazil
          date_start: '2014-04-01'
          date_end: '2016-03-01'
          description: |1-
            
            Dissertation: Role of cellular prion protein and its ligand, stip1, in the adult neurogenesis.
            Supported by: CNPq (2014 - 2016)
            
            Main techniques: primary cell culture, immunofluorescence, and hypothesis testing.
            
        ## -- BSc -- ##
        - title: Bachelor in Biological Science
          company: Universidade de São Paulo
          company_url: ''
          company_logo: ung
          location: São Paulo - SP, Brazil
          date_start: '2011-02-01'
          date_end: '2013-12-01'
          description: |1-
            
            Monography: Role of the interaction between the cellular prion protein and its ligand, STI1, in the biology of neural precursors from the murine adult brain.
            Supported by: University scholarship (2011 - 2012) and FAPESP (2012 - 2013)
            
            **Honor & Awards:**  
            - Best academic performance
            - Professor Bertha Lange de Morretes’ Award
            
    design:
      columns: '2'


  # - block: accomplishments
  #   content:
  #     # Note: `&shy;` is used to add a 'soft' hyphen in a long heading.
  #     title: 'Accomplish&shy;ments'
  #     subtitle:
  #     # Date format: https://docs.hugoblox.com/customization/#date-format
  #     date_format: Jan 2006
  #     # Accomplishments.
  #     #   Add/remove as many `item` blocks below as you like.
  #     #   `title`, `organization`, and `date_start` are the required parameters.
  #     #   Leave other parameters empty if not required.
  #     #   Begin multi-line descriptions with YAML's `|2-` multi-line prefix.
  #     items:
  #       - certificate_url: https://www.coursera.org
  #         date_end: ''
  #         date_start: '2021-01-25'
  #         description: ''
  #         icon: coursera
  #         organization: Coursera
  #         organization_url: https://www.coursera.org
  #         title: Neural Networks and Deep Learning
  #         url: ''
  #       - certificate_url: https://www.edx.org
  #         date_end: ''
  #         date_start: '2021-01-01'
  #         description: Formulated informed blockchain models, hypotheses, and use cases.
  #         icon: edx
  #         organization: edX
  #         organization_url: https://www.edx.org
  #         title: Blockchain Fundamentals
  #         url: https://www.edx.org/professional-certificate/uc-berkeleyx-blockchain-fundamentals
  #       - certificate_url: https://www.datacamp.com
  #         date_end: '2020-12-21'
  #         date_start: '2020-07-01'
  #         description: ''
  #         icon: datacamp
  #         organization: DataCamp
  #         organization_url: https://www.datacamp.com
  #         title: 'Object-Oriented Programming in R'
  #         url: ''
  #   design:
  #     columns: '2'


  # - block: collection
  #   id: posts
  #   content:
  #     title: Recent Posts
  #     subtitle: ''
  #     text: ''
  #     # Choose how many pages you would like to display (0 = all pages)
  #     count: 5
  #     # Filter on criteria
  #     filters:
  #       folders:
  #         - post
  #       author: ""
  #       category: ""
  #       tag: ""
  #       exclude_featured: false
  #       exclude_future: false
  #       exclude_past: false
  #       publication_type: ""
  #     # Choose how many pages you would like to offset by
  #     offset: 0
  #     # Page order: descending (desc) or ascending (asc) date.
  #     order: desc
  #   design:
  #     # Choose a layout view
  #     view: compact
  #     columns: '2'


  # - block: portfolio
  #   id: projects
  #   content:
  #     title: Projects
  #     filters:
  #       folders:
  #         - project
  #     # Default filter index (e.g. 0 corresponds to the first `filter_button` instance below).
  #     default_button_index: 0
  #     # Filter toolbar (optional).
  #     # Add or remove as many filters (`filter_button` instances) as you like.
  #     # To show all items, set `tag` to "*".
  #     # To filter by a specific tag, set `tag` to an existing tag name.
  #     # To remove the toolbar, delete the entire `filter_button` block.
  #     buttons:
  #       - name: All
  #         tag: '*'
  #       - name: Deep Learning
  #         tag: Deep Learning
  #       - name: Other
  #         tag: Demo
  #   design:
  #     # Choose how many columns the section has. Valid values: '1' or '2'.
  #     columns: '1'
  #     view: showcase
  #     # For Showcase view, flip alternate rows?
  #     flip_alt_rows: false


  # - block: markdown
  #   content:
  #     title: Gallery
  #     subtitle: ''
  #     text: |-
  #       {{< gallery album="demo" >}}
  #   design:
  #     columns: '1'


  # - block: collection
  #   id: featured
  #   content:
  #     title: Featured Publications
  #     filters:
  #       folders:
  #         - publication
  #       featured_only: true
  #   design:
  #     columns: '2'
  #     view: card


  - block: collection
    id: publications
    content:
      title: Publications
      text: |-
      #   {{% callout note %}}
      #   Quickly discover relevant content by [filtering publications](./publication/).
      #   {{% /callout %}}
      filters:
        folders:
          - publication
        exclude_featured: true
    design:
      columns: '2'
      view: compact


  - block: collection
    id: talks
    content:
      title: Talks
      filters:
        folders:
          - event
    design:
      columns: '2'
      view: compact


  - block: contact
    id: contact
    content:
      title: Contact
      subtitle:
      text: |-
        Feel free to contact me through this form:
      # Contact (add or remove contact options as necessary)
      email: cmcouto.silva@gmail.com
      # phone: +55 11 98671 1630
      # appointment_url: 'https://calendly.com'
      address:
        city: São Paulo
        region: Brazil
        country: Brazil
        country_code: BR
      # contact_links:
      #   - icon: twitter
      #     icon_pack: fab
      #     name: DM Me
      #     link: 'https://twitter.com/cmcoutosilva'
      # Automatically link email and phone or display as text?
      autolink: true
      # Email form provider
      form:
        provider: formspree
        formspree:
          id: xyyrwdbe
        netlify:
          # Enable CAPTCHA challenge to reduce spam?
          captcha: false
    design:
      columns: '2'
---
