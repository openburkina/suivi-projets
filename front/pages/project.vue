<template>
  <v-container style="margin-top: -90px">
    <v-row>
      <v-col cols="4"> </v-col>
      <v-col cols="4" class="text-center">
        <div class="info--text font-weight-bold display-2 mx-auto">Projects</div>
        <hr style="height: 5px; background: #2196f3; border-color: #2196f3; border-radius: 10px;" />
      </v-col>
      <v-col cols="4"> </v-col>
    </v-row>

    <v-row>
        <Chips></Chips>
    </v-row>
    <v-row>
      <v-data-table
        dense
        :headers="headers"
        :items="projects"
        item-key="name"
        class="elevation-1"
      ></v-data-table>
    </v-row>
  </v-container>
</template>

<script>
export default {
  head() {
    return {
      title: 'Project\'s list',
    }
  },
  data: () => ({
    projects: [
      {
        project_id: '00089459',
        title: 'Funding Facility for Stabilization',
        description:
          'To quickly respond to immediate needs of the areas which were under Islamic State of Iraq and Levant (ISIL) control and facilitate the process of return of internally displaced persons, this project provides stabilization support in Iraq.',
        expense: 109578406,
        budget: 317860856,
        country: 'Iraq',
      },
      {
        project_id: '00089137',
        title:
          'Law and Order Trust Fund for Afghanistan (LOTFA) - SUPPORT TO PAYROLL MANAGEMENT',
        description:
          'LOTFA Support to Payroll Management Project, provides exclusive support to fulfill the Ministry of Interior payroll management. This project was jointly developed by Government of Afghanistan, Ministry of Interior, UNDP, donors and other partners.',
        expense: 172346870,
        budget: 277968770,
        country: 'Afghanistan',
      },
      {
        project_id: '00130989',
        title: 'MINERD Equipos',
        description:
          'Acceso de la comunidad del sistema escolar público a las herramientas de la Tecnología de la Información y Comunicación (TICs) requeridas para expandir la formación escolar a distancia, en el contexto de la pandemia del COVID-19.',
        expense: 142123285,
        budget: 142151694,
        country: 'Dominican Republic',
      },
      {
        project_id: '00133885',
        title: 'Towards ending AIDS as a public threat by 2030',
        description: 'Towards Ending AIDS as a Public Health Threat by 2030',
        expense: 47484550,
        budget: 141226185,
        country: 'Zimbabwe',
      },
      {
        project_id: '00095446',
        title:
          'Apoyo al Plan Estratégico para Garantizar una vida Sana y Promover el Bienestar de toda la población de la Provincia de Buenos Aires, en todas las etapas de su ciclo de vida (2016/2019)',
        description:
          'Apoyo al Plan Estratégico para Garantizar una vida Sana y Promover el Bienestar de toda la población de la Provincia de Buenos Aires, en todas las etapas de su ciclo de vida (2016/2019)',
        expense: 71489164,
        budget: 126772809,
        country: 'Argentina',
      },
      {
        project_id: '00130447',
        title: 'Gestion Logistica MINERD',
        description:
          'Apoyo a la Digitalización de la Educación mediante la eficiencia en la gestión logística para asegurar el manejo y la distribución adecuada de los equipos necesarios para el fomento de las Tecnologías de la Información y Comunicación',
        expense: 29807844,
        budget: 84047464,
        country: 'Dominican Republic',
      },
      {
        project_id: '00135311',
        title: 'Tecnología e infraestructura al servicio de la inclusión',
        description:
          'Tecnología e infraestructura al servicio de la inclusión educativa',
        expense: 0,
        budget: 80070000,
        country: 'El Salvador',
      },
      {
        project_id: '00131699',
        title: 'Abordaje Comunitario contra el Hambre',
        description:
          'Abordaje Comunitario del Plan Nacional Argentina Contra el Hambre: el objetivo es favorecer la resignificación de la política alimentaria como instrumento de realización y restitución de derechos sociales y promoción de la sociedad organizada',
        expense: 46783807,
        budget: 69990968,
        country: 'Argentina',
      },
      {
        project_id: '00134183',
        title: 'Servicio Penitenciario Prov Bs As',
        description:
          'Apoyo al fortalecimiento de las capacidades institucionales del Servicio Penitenciario de la Provincia de Buenos Aires.',
        expense: 17167,
        budget: 68616665,
        country: 'Argentina',
      },
      {
        project_id: '00132175',
        title: 'Procurement Support Services to MoH, Phase 2',
        description:
          'At the request of the Ministry of Health, UNDP procures a range of medicines and medical products as an emergency measure, and builds the capacity needed to support a transparent, cost-effective procurement system for the Ministry of Health.',
        expense: 33953022,
        budget: 61295612,
        country: 'Ukraine',
      },
      {
        project_id: '00085156',
        title: 'Iraq Crisis Response and Resilience',
        description:
          'Iraq Crisis Response and Resilience is a programme that supports crisis response, and helps to strengthen resilience in Iraq.',
        expense: 12262251,
        budget: 59497861,
        country: 'Iraq',
      },
      {
        project_id: '00122295',
        title: 'Apoyo a las políticas estrategicas federales',
        description:
          'Programa de apoyo a las políticas estratégicas de carácter federal para la atención de la salud de la población, que comprendan la promoción, protección, asistencia, recuperación y rehabilitación de la salud.',
        expense: 0,
        budget: 54441443,
        country: 'Argentina',
      },
      {
        project_id: '00127162',
        title: 'Dominica Development and Reconstruction Facility',
        description:
          'Provides a transparent, predictable, coordinated and timely financial mechanism to accelerate recovery, reconstruction and development interventions.',
        expense: 27626381,
        budget: 49107735,
        country: 'Dominica',
      },
      {
        project_id: '00132041',
        title: 'COVID-19 RFF ExO',
        description: 'COVID-19 Rapid Financing Facility - ExO allotment',
        expense: 0,
        budget: 46873287,
        country: 'Office of the Administrator',
      },
      {
        project_id: '00130964',
        title: 'Fonds Mondial / Paludisme 2021-2023',
        description:
          'Le projet vise à soutenir les programmes nationaux de lutte contre le Paludisme pour accélérer la mise en œuvre du plan stratégique national afin de réduire le fardeau du Paludisme au Burundi',
        expense: 7911638,
        budget: 43399318,
        country: 'Burundi',
      },
      {
        project_id: '00105005',
        title: 'UN Electoral Support Project (UNESP)',
        description:
          'The UN Electoral Support Project is the international community’s programming vehicle to support the next elections in Afghanistan is supporting by the United Nation Development Programme UNDP.',
        expense: 4808238,
        budget: 37709740,
        country: 'Afghanistan',
      },
      {
        project_id: '00128680',
        title: 'Réponse au COVID-19 (EU)',
        description: 'Réponse solidaire européenne à la COVID-19 en Algérie.',
        expense: 8860913,
        budget: 34793300,
        country: 'Algeria',
      },
      {
        project_id: '00129732',
        title: 'Procurement for NCDs',
        description:
          'Procurement of medicines and health products for the control of noncommunicable diseases (NCD) in Turkmenistan through the United Nations Development Programme',
        expense: 1719184,
        budget: 32719298,
        country: 'Turkmenistan',
      },
      {
        project_id: '00106771',
        title: 'Yemen Crisis Response Project III',
        description:
          'World Bank Additional Support to Yemen Crisis Emergency Response which is a 24-month aims to mitigate the impact of the current crisis on local households and communities and assist their recovery from the bottom-up using local systems,',
        expense: 24523459,
        budget: 32700000,
        country: 'Yemen',
      },
      {
        project_id: '00131655',
        title: 'Support to Iraq´s Electoral Process – Capacity Develop',
        description:
          'Support to Iraq´s Electoral Process – Capacity Development\n The project aims at assisting IHEC with capacity building and support to various technical areas, both at headquarters and governorate level, in preparation for early elections of 2021',
        expense: 8977420,
        budget: 31049977,
        country: 'Iraq',
      },
      {
        project_id: '00118949',
        title:
          'Programa de apoyo para la eficiencia y la transparencia del proceso de modernización del documento nacional de identificación en Honduras',
        description:
          'Programa de apoyo para la eficiencia y la transparencia del proceso de modernización del documento nacional de identificación en Honduras',
        expense: 29211291,
        budget: 31012484,
        country: 'Honduras',
      },
      {
        project_id: '00114690',
        title: 'Appui au Processus Électoral en Haïti (PAPEH)',
        description:
          'Le projet dappui au Processus Electoral en Haiti 2019-2021 apporte des réponses adéquates aux besoins du CEP et autres acteurs du processus à travers lappui au renforcement des capacités de linstitution électorale.',
        expense: 7219923,
        budget: 30589948,
        country: 'Haiti',
      },
      {
        project_id: '00126787',
        title: 'COVID-19 CO Response',
        description:
          'The CO will strengthen national capacities to ensure attention is given to the needs of the most vulnerable people and guided by humanitarian principles of inclusion, gender, protection, and community participation principles.',
        expense: 6755408,
        budget: 29845367,
        country: 'Honduras',
      },
      {
        project_id: '00112026',
        title: 'Achieving 2030 Agenda for Sustainable Development in AP',
        description:
          'This Regional Project is designed as a framework for UNDP’s contributions to support countries in Asia and the Pacific to achieve eradication of poverty and significant reduction of inequalities and exclusion in a way that is sustainable and resilient.',
        expense: 13977064,
        budget: 28856524,
        country: 'Rgnl Center in Bangkok (RCB)',
      },
      {
        project_id: '00100737',
        title: 'Cobertura de Salud Universal Efectiva',
        description:
          'Programa de apoyo a la Cobertura de Salud Universal Efectiva garantizando la cobertura prestacional mediante la provisión de insumos críticos',
        expense: 5242470,
        budget: 28347551,
        country: 'Argentina',
      },
      {
        project_id: '00127475',
        title: 'Support to COVID-19 Response',
        description:
          'COVID-19 Response Plan for Nigeria with the objective to ensure optimum care of confirmed COVID-19 cases and contain the spread of the outbreak through an inclusive and nationally owned process and based on emerging best practices.',
        expense: 18659027,
        budget: 27874181,
        country: 'Nigeria',
      },
      {
        project_id: '00102396',
        title: 'Recovery and Peacebuilding Programme',
        description:
          'The programme aims to overcome the consequences of the military conflict in Ukraine and to provide a foundation for a rapid transition to sustainable recovery of the conflict-affected regions.',
        expense: 15298615,
        budget: 27558128,
        country: 'Ukraine',
      },
      {
        project_id: '00074638',
        title: 'Global Health Innovative Tech Research and Development',
        description:
          'Global Health Innovative Technology Research and Development - Accelerating access and delivery of new health technologies for tuberculosis, malaria and neglected tropical diseases: supporting countries to achieve universal health coverage.',
        expense: 6742289,
        budget: 27478556,
        country: 'Bureau Policy & Prog Support',
      },
      {
        project_id: '00107033',
        title: 'Mejorando la Eficiencia y la Calidad del Sector Educativo',
        description:
          'Mejorando la Eficiencia y la Calidad del Sector Educativo en Panama en la asignación de recursos y orientar las decisiones de política educativa a través de una transformación digital de los sistemas de información del Ministerio',
        expense: 9168450,
        budget: 26692602,
        country: 'Panama',
      },
      {
        project_id: '00108620',
        title: 'Global Funds programme continuation',
        description:
          'continuing the implementation of current Global Fund grants for an additional three years under the same goals, strategic objectives and similar programmatic interventions.',
        expense: 10966134,
        budget: 25535049,
        country: 'Sudan, Republic of the',
      },
      {
        project_id: '00116194',
        title: 'BRA/19/005 - GCF REDD+ Brazil',
        description:
          'BRA/19/005 - REDD+ results-based payments for results achieved by Brazil in the Amazon biome in 2014 and 2015',
        expense: 455133,
        budget: 25415135,
        country: 'Brazil',
      },
      {
        project_id: '00065799',
        title: 'Supporting Lebanese Hosting Communities',
        description:
          'Support to economic recovery, community security and social cohesion in Lebanese communities affected by the Syrian Crisis',
        expense: 15968292,
        budget: 24823242,
        country: 'Lebanon',
      },
      {
        project_id: '00121215',
        title: '7th Operational Phase of the GEF Small Grants Programme',
        description:
          'PIMS6271 - 7th Operational Phase of the GEF Small Grants Programme',
        expense: 20081701,
        budget: 23865711,
        country: 'Bureau Policy & Prog Support',
      },
      {
        project_id: '00116957',
        title: 'Joint UNDP-DPPA Programme on conflict prevention',
        description:
          'Joint UNDP-DPPA Programme on building national capacities for conflict prevention deploys Peace and Development Advisors (PDAs) in fragile countries and supports Resident Coordinators (RCs) and UNCTs.',
        expense: 13407099,
        budget: 23104124,
        country: 'Crisis Response Unit',
      },
      {
        project_id: '00117580',
        title: 'Electoral Support Project',
        description:
          'A project is being implemented to support the National Election Board of Ethiopia (NEBE) to ensure credible, inclusive and peaceful general elections which will take place in 2021.',
        expense: 16707758,
        budget: 22312102,
        country: 'Ethiopia',
      },
      {
        project_id: '00136333',
        title: 'HIV MAL & TB NFM3 BENGUELA CUANZA SUL',
        description:
          'The Project seeks to establish a robust integrated HIV/Malaria and TB system and response in the provinces of Benguela and Cuanza Sul, while ensuring that the approaches adopted are compatible with the national health system.',
        expense: 914574,
        budget: 22261910,
        country: 'Angola',
      },
      {
        project_id: '00036408',
        title: 'DESARROLLO METROPOLITANO MUNICIPALIDAD DE GUATEMALA',
        description:
          'PROGRAMA DE DESARROLLO METROPOLITANO DE LA MUNICIPALIDAD DE GUATEMALA',
        expense: 10715332,
        budget: 22238205,
        country: 'Guatemala',
      },
      {
        project_id: '00075077',
        title: 'EFICACIA Y EFICIENCIA EN USO DE RECURSOS REGALIAS',
        description:
          'Fortalecer las capacidades de gestión pública territorial y nacional en el uso eficaz y eficiente de los recursos provenientes del Sistema General de Regalías (SGR)',
        expense: 11493545,
        budget: 22050304,
        country: 'Colombia',
      },
      {
        project_id: '00123140',
        title: 'Stabilization Facility-Nigeria Window',
        description:
          'The Facility act as a rapid-response package, aiming to achieve the immediate stabilisation of specific target areas in North East Nigeria, cleared of Boko Haram control, but where communities remain vulnerable to continued infiltration and attack.',
        expense: 13465212,
        budget: 21829146,
        country: 'Nigeria',
      },
      {
        project_id: '00134271',
        title: 'Integrating Services for Maximum Impact',
        description:
          'Expanding and Enhancing quality TB and HIV prevention, care and control in the Republic of South Sudan.',
        expense: 12581372,
        budget: 21515197,
        country: 'South Sudan, Republic of',
      },
      {
        project_id: '00128217',
        title: 'Emergency Social Protection Enhancement & COVID19 Respon',
        description:
          'The project aims to provide nutrition-sensitive cash transfers, temporary employment, and increased access to basic services and economic opportunities as well as to strengthen the capacity of national service delivery institutions.',
        expense: 4538233,
        budget: 20000000,
        country: 'Yemen',
      },
      {
        project_id: '00084928',
        title: 'Inception Phase - National Urban Poverty Reduction Programme',
        description:
          'National Urban Poverty Reduction Programme (NUPRP) will initially focus on up to 36 cities/towns in two phases throughout 2016-2022.',
        expense: 11051583,
        budget: 18400000,
        country: 'Bangladesh',
      },
      {
        project_id: '00127056',
        title: 'Response Facility_COVID-19',
        description:
          'UNDP will conduct SEI&NA on the economy, boost health procurement, volunteerism, digital, and acceleration. RM opportunities and partnerships for advancing programme activities mitigating COVID-19 impact and beyond will be explored.',
        expense: 4871738,
        budget: 18332348,
        country: 'Belarus, Republic of',
      },
      {
        project_id: '00118265',
        title: 'Peace Support Facility',
        description:
          'Peace Support Facility (PSF) project to support the political process in Hodeidah governorate',
        expense: 3289408,
        budget: 18176803,
        country: 'Yemen',
      },
      {
        project_id: '00089434',
        title: 'Zimbabwe Resilence Building Fund',
        description:
          'Increased capacities of communities to protect development gains and achieve improved well-being outcomes in the face of shocks and stresses enabling them to contribute to the economic growth of Zimbabwe',
        expense: 9852343,
        budget: 18142351,
        country: 'Zimbabwe',
      },
      {
        project_id: '00095107',
        title: 'Health For Development',
        description:
          'This award is for outputs under health and development portfolio s per UNDP Sudan CPD pillars',
        expense: 3027615,
        budget: 17579500,
        country: 'Sudan, Republic of the',
      },
      {
        project_id: '00128893',
        title: 'Apoyo al Programa RISP-HO COVID-19',
        description:
          'Proyecto Respuesta Inmediata de Salud Pública para Contener y Controlar el Coronavirus (COVID-19) y Mitigar su Efecto en la Prestación de Servicios en Honduras (RISP-HO)',
        expense: 1071044,
        budget: 16542945,
        country: 'Honduras',
      },
      {
        project_id: '00133810',
        title: 'Support Services Ministry of Health 2021 to 2023',
        description:
          'Support to the implementation of the TB and Malaria grants managed by the Ministry of Health and Child Care in Zimbabwe',
        expense: 3586456,
        budget: 16458427,
        country: 'Zimbabwe',
      },
      {
        project_id: '00101442',
        title:
          'Fonds National REDD+ de la RDC -Programme d’Appui à la Société Civile',
        description:
          'Ce programme contribue à la bonne gouvernance du programme REDD+ en Republique democratique du Congo',
        expense: 6442291,
        budget: 16213494,
        country: 'Democratic Republic of Congo',
      },
      {
        project_id: '00098752',
        title: 'GAVI Phase II-Improving vaccination systems',
        description:
          'Improving efficiency of vaccination systems through operationalisation of web based vaccine management system in all the districts of select states',
        expense: 9900539,
        budget: 16190763,
        country: 'India',
      },
      {
        project_id: '00122248',
        title: 'Strengthen Institutional & Economic Resilience (SIERY)',
        description:
          'Strengthening of Institutional and Economic Recovery in Yemen (SIERY) aims to improve economic & social wellbeing for Yemeni, building resilience & good governance, strengthening Humanitarian-Development Nexus & supporting Private Sector Development.',
        expense: 2010504,
        budget: 16181092,
        country: 'Yemen',
      },
      {
        project_id: '00061324',
        title: 'PIMS 4561 GEF-SGP Operational Phase 5',
        description:
          'PIMS 4561 - This project will provide support to communities through small grants by continuing the Small Grants Programme its fifth Operational Phase.',
        expense: 2551069,
        budget: 16132575,
        country: 'Bureau Policy & Prog Support',
      },
      {
        project_id: '00096954',
        title:
          'Mejora de la capacidad del Ministerio de Finanzas de Cordoba como organismo rector de los procesos de innovacion y getion por medio de las Tecnologias de la Informacion y la Comunicacion.',
        description:
          'Objetivo del proyecto: mejorar la capacidad de gestión de diversas áreas del Ministerio de Finanzas para favorecer la modernización de la provincia de Córdoba con mayor eficacia, eficiencia y transparencia a través de la incorporación de TICS.',
        expense: 3978342,
        budget: 15770017,
        country: 'Argentina',
      },
      {
        project_id: '00086948',
        title: 'Crisis Response Unit Management',
        description:
          'Crisis Response Unit - Organizational Effectiveness - effectiveness and capacity is enhanced in order to achieve expected results',
        expense: 8974599,
        budget: 15499727,
        country: 'Crisis Response Unit',
      },
      {
        project_id: '00090372',
        title: 'GEF-SGP Operational Phase 6',
        description:
          'GEF-SGP OP6 will target its support towards priority landscapes and seascapes for community based conservation actions, promote sustainable energy access co-benefits, climate smart agro-ecology, and local to global chemicals coalitions.',
        expense: 739803,
        budget: 15454137,
        country: 'Bureau Policy & Prog Support',
      },
      {
        project_id: '00138403',
        title: 'Sehatmandi Project',
        description:
          'Sustaining the Basic Package of Health Services in Afghanistan (BPHS) and Essential Package of Hospital Services (EPHS) in Afghanistan',
        expense: 0,
        budget: 15000000,
        country: 'Afghanistan',
      },
      {
        project_id: '00104158',
        title: 'Resilience and Recovery',
        description:
          'Put the country on a more robust development path by helping the local authorities to restore security, essential services delivery and livelihoods opportunities.',
        expense: 4840275,
        budget: 14921273,
        country: 'Libya',
      },
      {
        project_id: '00102590',
        title: 'Scaling-up of GLOF Risk Reduction in North Pakistan',
        description:
          'Scaling-up of Glacial Lake Outburst Flood (GLOF) Risk Reduction in Northern Pakistan',
        expense: 3161792,
        budget: 14865513,
        country: 'Pakistan',
      },
      {
        project_id: '00116893',
        title: 'État de droit, Sécurité et Cohésion sociale',
        description:
          'Le programme vise le développement d’un Burkina Faso pacifique et inclusif qui œuvre à la promotion d’une sécurité humaine partagée et au renforcement de la justice et des droits de l’homme.',
        expense: 2937077,
        budget: 14347925,
        country: 'Burkina Faso',
      },
      {
        project_id: '00122500',
        title: 'Managing Agent of the Sudan Humanitarian Fund',
        description:
          'Sudan Humanitarian Fund SHF 2019-UNDP-NGOs-SA2. This project has been established in line with UNDP’s role as Managing Agent of the Sudan Humanitarian Fund.',
        expense: 12985299,
        budget: 14328738,
        country: 'Sudan, Republic of the',
      },
      {
        project_id: '00090474',
        title: 'Procurement Support Services to Ministry of Health',
        description:
          'At the request of the MoH, UNDP procures a range of medicines and medical products as an emergency measure, and builds the capacity needed to support a transparent, cost-effective procurement system for the Ministry.',
        expense: 22519095,
        budget: 14044477,
        country: 'Ukraine',
      },
      {
        project_id: '00112695',
        title:
          'Programme d’Appui à la Lutte Antipaludique au Tchad – Phase III ',
        description:
          'Le projet PALAT III s’inscrit dans le cadre du financement du Fonds mondial pour la lutte contre le paludisme au Tchad pour la période allant du 1er juillet 2018 au 30 juin 2021',
        expense: 14563989,
        budget: 13937517,
        country: 'Chad',
      },
      {
        project_id: '00129553',
        title: 'Fonds Mondial VIH/Tuberculose 2021-2023',
        description:
          'Le projet vise à soutenir les programmes nationaux de lutte contre la tuberculose et le VIH pour accélérer la mise en œuvre du plan stratégique national afin de réduire le fardeau du VIH et de la tuberculose au Burundi',
        expense: 3516956,
        budget: 13901742,
        country: 'Burundi',
      },
      {
        project_id: '00108446',
        title: 'Turkey Resilience Project in response to the SyriaCrisis',
        description:
          'This proposal aims to strengthen the economic and social resilience of the individuals and institu-tions in the provinces that are most affected by the influx of Syrian refugees.',
        expense: 9345229,
        budget: 13879935,
        country: 'Turkey',
      },
      {
        project_id: '00120458',
        title: 'Investment Programme for Resilience',
        description:
          'The resilience of marginalized Palestinian communities is reinforced, through addressing the immediate needs of the COVID-19 crisis and mitigating the medium- to longer-term socio-economic effects in the areas of health, community and employment.',
        expense: 8532622,
        budget: 13847466,
        country: 'Prog for Palestinian People',
      },
      {
        project_id: '00121665',
        title: 'Moz Recovery Facility',
        description:
          'The UNDP Recovery Facility has been developed in the aftermath of Cyclones Idai and Kenneth, aiming to contribute to Mozambique’s rapid restoration of development pathways in a manner that builds resilience to disasters.',
        expense: 5149629,
        budget: 13766604,
        country: 'Mozambique',
      },
      {
        project_id: '00063928',
        title: 'Global HIV, Health and Development Project',
        description:
          'Policy and technical support to address development dimensions of HIV and health. UNDP’s work in HIV and health is guided by the 2030 Agenda for Sustainable Development & the UNDP Strategic Plan 2018-2021.',
        expense: 4985800,
        budget: 13765805,
        country: 'Bureau Policy & Prog Support',
      },
      {
        project_id: '00094616',
        title: 'Immediate Stabilization Facility for Libya',
        description:
          'This project will support the Government of National Accord (GNA) to deliver basic services and develop legitimacy by contributing to recovery and peace efforts.',
        expense: 11117532,
        budget: 13673965,
        country: 'Libya',
      },
      {
        project_id: '00130819',
        title: 'HC - NFM3 Malaria',
        description:
          'The project is inteded to support malaria control in Guinea-Bissau',
        expense: 3065483,
        budget: 13656436,
        country: 'Guinea-Bissau',
      },
      {
        project_id: '00101619',
        title: 'Technical Assistance to REDD+ Implementation',
        description:
          'Technical Assistance to implementation of United Nations Programme on Reducing Emissions from Deforestation and Forest Degradation',
        expense: 3701692,
        budget: 13463246,
        country: 'Bureau Policy & Prog Support',
      },
      {
        project_id: '00124821',
        title: 'Effective TB and HIV control progr in the Kyrgyz Republi',
        description:
          'Programme aims to further reduce TB and HIV burden through ensuring universal access to timely and quality HIV and TB diagnosis and treatment, HIV prevention focused on KAPs, care and support to PLHIV.',
        expense: 2902067,
        budget: 13340067,
        country: 'Kyrgyzstan',
      },
      {
        project_id: '00126861',
        title: 'EU4Schools phase I',
        description:
          'The overall objective of the action is to support national and local governments in reducing further social and economic losses, and to accelerate the recovery process through educational facility repairs and reconstruction.',
        expense: 6897027,
        budget: 13329028,
        country: 'Albania',
      },
      {
        project_id: '00129706',
        title: 'EU4Schools Phase II',
        description: 'EU4Schools Phase II',
        expense: 4737642,
        budget: 13170298,
        country: 'Albania',
      },
      {
        project_id: '00106781',
        title: 'UNDP NDC Support Programme',
        description:
          'This Global Programme was created to support Governments to achieve transformational change by using NDC implementation as a mechanism to scale up investments in climate change and deliver sustainable development.',
        expense: 4043298,
        budget: 12916513,
        country: 'Bureau Policy & Prog Support',
      },
      {
        project_id: '00133855',
        title: 'Reactive Colombia',
        description:
          'This project will enable socioeconomic reactivation by supporting: Livelihoods stabilization for individuals and communities affected by the COVID-19 economic crisis by ensuring that relief, recovery, and development are addressed simultaneously.',
        expense: 440697,
        budget: 12790902,
        country: 'Colombia',
      },
      {
        project_id: '00131766',
        title: 'COVID-19 Response FBIH WB loan to BIH',
        description:
          'Response to COVID-19 pandemic in Federation of Bosnia and Herzegovina',
        expense: 3553316,
        budget: 12654425,
        country: 'Bosnia and Herzegovina',
      },
      {
        project_id: '00126434',
        title: 'Accel. Clean Energy Access to Reduce Inequality (ACCESS)',
        description:
          'Accelerating Clean Energy Access to Reduce Inequality (ACCESS) aims to support equitable and sustainable access to basic services for livelihood improvements',
        expense: 526093,
        budget: 12602325,
        country: 'Indonesia',
      },
      {
        project_id: '00090196',
        title: 'PAZ SOSTENIBLE',
        description:
          'Contribuir, en asocio con las instituciones, la sociedad civil y la cooperación internacional, a la implementación de la Agenda 2030 en Colombia (especialmente el Objetivo 16) en el territorio',
        expense: 5909055,
        budget: 12567349,
        country: 'Colombia',
      },
      {
        project_id: '00084981',
        title:
          'Consolidación del modelo de atención primaria de la salud a través de la provisión y dispensa de medicamentos esenciales',
        description:
          'Consolidación del modelo de atención primaria de la salud a través de la provisión y dispensa de medicamentos esenciales – Proyectos BID',
        expense: 567363,
        budget: 12284396,
        country: 'Argentina',
      },
      {
        project_id: '00122666',
        title: 'Malaria Prevention and Case Management',
        description:
          'Strengthening and Scaling up Malaria Prevention and Case Management to Improve Health Status in Afghanistan supported by the Global Fund project in Afghanistan.',
        expense: 1574717,
        budget: 12193102,
        country: 'Afghanistan',
      },
      {
        project_id: '00122786',
        title: 'Mejoramiento Gran Mercado de Belen 2 Fase',
        description:
          'Mejoramiento del servicio de comercialización del Gran Mercado de Belén 2ª\nFase, Iquitos, Provincia de Maynas, Departamento de Loreto',
        expense: 314373,
        budget: 12129480,
        country: 'Peru',
      },
      {
        project_id: '00107518',
        title: 'Support to Universal Suffrage Elections in Somalia',
        description:
          'UNDP/UNSOM Joint Programme for Support to Universal Suffrage Elections in the Federal Republic of Somalia',
        expense: 3334791,
        budget: 12003416,
        country: 'Somalia',
      },
      {
        project_id: '00130866',
        title: 'Building Resilience through Employment Promotion (BREP)',
        description:
          'Strengthening Resilience and Socio-economic Inclusion through Employment Creation in Crisis-affected Communities of Iraq',
        expense: 1364568,
        budget: 11829140,
        country: 'Iraq',
      },
      {
        project_id: '00135717',
        title: 'Global Funds HIV Pakistan',
        description:
          'Accelerated response to HIV through effective prevention, treatment, care and support interventions for Key Populations',
        expense: 217240,
        budget: 11753666,
        country: 'Pakistan',
      },
      {
        project_id: '00098771',
        title:
          'Community-Based Agriculture and Rural Development - East (CBARD-E)',
        description:
          'Community-Based Agriculture and Rural Development - East (CBARD-E)\nTo prove the viability of high-value agricultural-based interventions in improving local economies in Nangarhar as a sustainable alternative to illicit crop cultivation.',
        expense: 2018553,
        budget: 11627934,
        country: 'Afghanistan',
      },
      {
        project_id: '00106358',
        title: 'Biodiversity Finance Initiative (BIOFIN) Phase II',
        description:
          'The Biodiversity Finance Initiative (BIOFIN) Phase II aims to produce improved biodiversity and development outcomes and to contribute to filling the finance gap through the implementation of Biodiversity Finance Solutions.',
        expense: 3830444,
        budget: 11593532,
        country: 'Bureau Policy & Prog Support',
      },
      {
        project_id: '00090590',
        title: 'Emergency support to Govt CAM in fight against COVID19',
        description:
          'Support to the Royal Government of Cambodia to Respond to Covid-19 Pandemic through the Provision of Health and Laboratory Equipment',
        expense: 234811,
        budget: 11590599,
        country: 'Cambodia',
      },
      {
        project_id: '00085200',
        title: 'Hydro chlorofluorocarbons phase out management plan (HPMP)',
        description:
          'The hydro chlorofluorocarbons phase out management plan (HPMP) - Phase II will enable India to achieve compliance with Montreal Protocol',
        expense: 6200344,
        budget: 11523500,
        country: 'India',
      },
      {
        project_id: '00113685',
        title: 'Rehabilitation of Social Services and Infrastructure',
        description: 'Enhancing Humanitarian Recovery and Resilience.',
        expense: 2827835,
        budget: 11496110,
        country: 'Syria',
      },
      {
        project_id: '00059882',
        title: 'POLITICAS MUNICIPALES DE JUVENTUD',
        description:
          'El proyecto pretende contruibuir a la promoción y tutela de los derechos fundamentales de los jóvenes, para la prevensión de todas las formas de discriminación y marginalización.',
        expense: 6504958,
        budget: 11382283,
        country: 'Guatemala',
      },
      {
        project_id: '00122756',
        title: 'REDD+ Pagos Basados en Resultados',
        description:
          'Costa Rica REDD+ Pagos Basados en Resultados para el período de resultados 2014-2015',
        expense: 315946,
        budget: 11365470,
        country: 'Costa Rica',
      },
      {
        project_id: '00116311',
        title: 'Prog. for EQ & Tsunami Infrastruc. Recon. Asst. (PETRA)',
        description:
          'Indonesia, Sulawesi/Lombok Programme for Earthquake and Tsunami Infrastructure Reconstruction Assistance (PETRA)',
        expense: 6060989,
        budget: 11214229,
        country: 'Indonesia',
      },
      {
        project_id: '00099753',
        title: 'Emergency Mine Action',
        description:
          'Emergency Mines Clearance to reduce the socio-economic impact of explosive remnants of war and mines on people and communities.',
        expense: 9356669,
        budget: 10888684,
        country: 'Yemen',
      },
      {
        project_id: '00114502',
        title: 'BRA/18/019 - Sistema Prisional e Socieducativo CNJ',
        description:
          'BRA/18/019 - Fortalecimento do Monitoramento e da Fiscalização do Sistema Prisional e Socioeducativo (CNJ)',
        expense: 7387145,
        budget: 10721532,
        country: 'Brazil',
      },
      {
        project_id: '00108414',
        title: 'Support Services to Ministry of Health',
        description:
          'Support to the implementation of the TB and Malaria grants managed by the Ministry of Health and Child Care in Zimbabwe',
        expense: 7299865,
        budget: 10709563,
        country: 'Zimbabwe',
      },
      {
        project_id: '00124739',
        title: 'SIDA UNDP Strategic Collaboration on Env and CC',
        description: 'SIDA UNDP Strategic Collaboration on Env and CC',
        expense: 4647005,
        budget: 10609060,
        country: 'Bureau Policy & Prog Support',
      },
      {
        project_id: '00107433',
        title: 'Embarazo Adolescente',
        description:
          'Apoyo al Plan Nacional de Prevención y Reducción del Embarazo No Intencional en la Adolescencia',
        expense: 2726078,
        budget: 10562210,
        country: 'Argentina',
      },
      {
        project_id: '00129730',
        title: 'Projet dappui au renforct de la riposte nationale au VI',
        description:
          'Ce projet est créée pour lutter contre le VIH et la Tuberculose à travers la subvention du Fonds Mondial pour le Congo au cours du cycle 2021-2023.',
        expense: 3793082,
        budget: 10137504,
        country: 'Congo',
      },
      {
        project_id: '00095226',
        title: 'BRA/16/004 - Support to Education &Training in Haiti',
        description:
          'BRA/16/004 - Support to Technical and Vocational Education and Training in Haiti through the Establishment of a Vocational Training Center and Related Institutional Strengthening.',
        expense: 1134837,
        budget: 10062457,
        country: 'Brazil',
      },
      {
        project_id: '00127222',
        title: 'CSMT Engagement Facility',
        description:
          'This project aims to enable the Crisis Bureau and, more broadly, the Global Policy Network to provide integrated, coherent and timely support to the Country Offices especially in crisis-setting. The project is managed by the CSMT.',
        expense: 9532736,
        budget: 10027636,
        country: 'Crisis Response Unit',
      },
    ],
    headers: [
      {
        text: 'ID',
        align: 'start',
        sortable: false,
        value: 'project_id',
      },
      { text: 'Project Title', value: 'title' },
      { text: 'Country Office / Operating Unit', value: 'country' },
      { text: 'Budget', value: 'budget' },
      { text: 'Expense', value: 'expense' },
    ],
  }),
}
</script>

