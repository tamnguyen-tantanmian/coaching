# Positioning, Concept and Architecture for a JTL Multi-Shop SaaS Application (Shop 6.0)
Kamp-Lintfort, Berlin, HCMC 31.03.2026

## Table of Contents

- [Disclaimer](#disclaimer)
- [About Coduct Solutions](#about-coduct-solutions)
- [1 Executive Summary](#1-executive-summary)
- [2 Orientation within the Document](#2-orientation-within-the-document)
  - [Target-Group-Oriented Reading Recommendations](#target-group-oriented-reading-recommendations)
- [3 Engagement](#3-engagement)
  - [3.1 Initial Situation and Motivation](#31-initial-situation-and-motivation)
  - [3.2 Target vision](#32-target-vision)
- [4 Market and technology analysis](#4-market-and-technology-analysis)
  - [4.1 Technological development in e-commerce](#41-technological-development-in-e-commerce)
  - [4.2 Market Structure and Key Vendor Groups](#42-market-structure-and-key-vendor-groups)
- [5 Positioning of JTL-Shop 6.0](#5-positioning-of-jtl-shop-60)
- [6 Functional and technical requirements](#6-functional-and-technical-requirements)
  - [6.1 API-First, interfaces, role model WaWi and shop / multichannel](#61-api-first-interfaces-role-model-wawi-and-shop--multichannel)
  - [6.2 Regional and Regulatory Requirements](#62-regional-and-regulatory-requirements)
  - [6.3 Ease of Use and Administrative Convenience](#63-ease-of-use-and-administrative-convenience)
  - [6.4 Multi-tenancy, Multi-shop Structure, Code Reuse](#64-multi-tenancy-multi-shop-structure-code-reuse)
  - [6.5 User Experience and Visual Design, Headless PWA Frontend](#65-user-experience-and-visual-design-headless-pwa-frontend)
  - [6.6 Updates, Extensibility, and Ecosystem](#66-updates-extensibility-and-ecosystem)
  - [6.7 AI Capabilities & Agentic Commerce Perspectives](#67-ai-capabilities--agentic-commerce-perspectives)
- [7 Architecture Overview](#7-architecture-overview)
  - [7.1 Layer Model](#71-layer-model)
  - [7.2 Software Lifecycle Management](#72-software-lifecycle-management)
- [8 Technical Architecture](#8-technical-architecture)
  - [8.1 Azure-First Cloud-Native Strategy](#81-azure-first-cloud-native-strategy)
  - [8.2 Cache-First Performance Philosophy](#82-cache-first-performance-philosophy)
  - [8.3 Logical Shop Isolation and Escalation Path](#83-logical-shop-isolation-and-escalation-path)
  - [8.4 Deterministic Rendering and SEO Governance](#84-deterministic-rendering-and-seo-governance)
  - [8.5 Upgrade-Safe Contracts and Versioning](#85-upgrade-safe-contracts-and-versioning)
  - [8.6 ERP-Agnostic Connector Architecture](#86-erp-agnostic-connector-architecture)
  - [8.7 High-Level Platform Architecture and End-to-End Flow](#87-high-level-platform-architecture-and-end-to-end-flow)
  - [8.8 Rationale for technology stacks, services, AI-assisted development](#88-rationale-for-technology-stacks-services-ai-assisted-development)
  - [8.9 Rendering and SEO architecture](#89-rendering-and-seo-architecture)
  - [8.10 Themes and template architecture](#810-themes-and-template-architecture)
  - [8.11 Extensions Platform](#811-extensions-platform)
  - [8.12 Multi-Tenant, Shop, Locale, and Currency Model](#812-multi-tenant-shop-locale-and-currency-model)
  - [8.13 Domain and Routing Architecture](#813-domain-and-routing-architecture)
  - [8.14 Data and Storage Architecture](#814-data-and-storage-architecture)
  - [8.15 Caching Architecture](#815-caching-architecture)
  - [8.16 Event and Synchronization Model](#816-event-and-synchronization-model)
  - [8.17 Security and Isolation Model](#817-security-and-isolation-model)
  - [8.18 Operating Model and Scalability](#818-operating-model-and-scalability)
  - [8.19 Architectural Constraints and Non-Goals](#819-architectural-constraints-and-non-goals)
- [9 Implementation of JTL Shop 6.0 and MVP](#9-implementation-of-jtl-shop-60-and-mvp)
  - [9.1 Features and MVP scope](#91-features-and-mvp-scope)
  - [9.2 MVP Estimate](#92-mvp-estimate)
  - [9.3 Team Setup](#93-team-setup)
  - [9.4 Roadmap and Milestones](#94-roadmap-and-milestones)
- [10 Conclusion](#10-conclusion)
- [Appendix: Challenges and Proposed Solutions](#appendix-challenges-and-proposed-solutions)
  - [On-Premises Operation of JTL-WaWi in a Cloud Context](#on-premises-operation-of-jtl-wawi-in-a-cloud-context)
  - [Sync Load on WaWi](#sync-load-on-wawi)
  - [Schema Changes in the Future PIM](#schema-changes-in-the-future-pim)
  - [Proposed Solutions](#proposed-solutions)
  - [API Rate Limit of JTL-WaWi](#api-rate-limit-of-jtl-wawi)
  - [Proposed Solutions](#proposed-solutions)
  - [Release cycle of JTL-WaWi](#release-cycle-of-jtl-wawi)
  - [Approaches to solutions](#approaches-to-solutions)
  - [Frontend connector as the central stability layer in the release cycle](#frontend-connector-as-the-central-stability-layer-in-the-release-cycle)
  - [Proposed AI tools](#proposed-ai-tools)
- [Appendix: Team roles](#appendix-team-roles)
  - [Team roles overview](#team-roles-overview)
  - [Responsibilities / areas of accountability Required skills Delivery Lead (Level: Lead)](#responsibilities--areas-of-accountability-required-skills-delivery-lead-level-lead)
  - [Product Owner/Project Manager (PO/PM) (Level: Advanced)](#product-ownerproject-manager-popm-level-advanced)
  - [UI/UX Designer (Level: Advanced)](#uiux-designer-level-advanced)
- [Appendix: High-Level Request Architecture](#appendix-high-level-request-architecture)
- [Appendix: Infrastructure Request Flow](#appendix-infrastructure-request-flow)
- [Appendix: Single-Region MVP Architecture](#appendix-single-region-mvp-architecture)
- [List of Figures](#list-of-figures)
- [List of Tables](#list-of-tables)
- [List of Abbreviations](#list-of-abbreviations)
- [Bibliography](#bibliography)

## Disclaimer
This document was prepared by Coduct Solutions GmbH for JTL-Software-GmbH and serves the purpose of discussing and presenting relevant conceptual and software architecture decisions for a Shop 6.0 MVP. The information and recommendations contained in this document have been prepared to the best of our knowledge and belief, taking into account current technological standards and JTL's state of knowledge. No warranty is assumed for the completeness, accuracy, or suitability of this information for purposes other than those stated. Likewise, this document does not constitute a binding offer, a commitment, or a service description. Changes in technology or in the requirements of JTL-Software-GmbH may necessitate adjustments.

## About Coduct Solutions
Coduct Solutions GmbH is a Germany-based technology, outsourcing, and SaaS service provider with locations in NRW and Berlin. As a partner for business transformations, software development, and software modernisation, we create added value by activating bound resources. Our employees possess comprehensive technological competencies, particularly in the field of cloud transformation. Technology is at the centre of the change we drive forward with strong partnerships within our corporate group (including locations in Vietnam). So that our clients can focus their energy on their strategic core functions, we bring extensive project experience and well-founded capabilities across diverse industries and business areas into a collaborative partnership. Our website address is www.coduct.com.

Contributors:

Benjamin Buchhorn Pierrick Libert Manh Pham

Martin Sperling

Adrian Strahlke

## 1 Executive Summary
The document defines the strategic and functional foundation for the JTL-Shop 6.0 as a cloud-based multi-shop SaaS platform and positions it within the current e-commerce market environment.

The goal is a scalable commerce solution that leverages the process strengths of the JTL-WaWi as a differentiating feature while simultaneously meeting the product and growth expectations of modern retailers. The market analysis shows that competitive advantages arise not primarily from feature breadth, but from structural product decisions — particularly in the dimensions of multi-shop capability, ERP centrality, time-to-market, and economic scalability.

JTL-Shop 6.0 targets professional mid-market retailers and growing retail organisations that serve multiple channels, brands, or countries and rely on the JTL-WaWi as the strong operational core of their business. For this target group, maximum feature breadth or full enterprise freedom matters less than an economically operable, upgrade-capable platform with strong process proximity and better usability. The JTL-WaWi remains the operational core, while the shop serves as a separate experience and extension layer. Multi-shop is not an add-on but a first-class product feature, enabling multiple shops to be operated from a single backend without development, operational, or support effort increasing linearly.

Architecturally, JTL-Shop 6.0 is designed as a cloud-based multi-shop SaaS platform with decoupled headless frontends and an API-first architecture. The JTL-WaWi remains the leading ERP system and central data source; support for both on-premise and future cloud-based WaWi variants, as well as an Azure-based infrastructure with a focus on scalability, fault tolerance, and automation, form the foundation for a long-term expandable and AI-supporting platform.

In this way, JTL-Shop 6.0 addresses the gap between global SaaS providers and enterprise composable solutions. While SaaS platforms offer rapid usability and scalability but frequently lose depth of process, enterprise composable solutions enable maximum flexibility at significantly higher cost and greater complexity. JTL-Shop 6.0 combines fast time-to-market and ecosystem capability with robust process logic and clear responsibilities, so that growth does not automatically lead to increasing integration, operational, and governance overhead.

The Minimum Viable Product (MVP) for JTL-Shop 6.0 elaborated in this document describes a functionally and technically highly flexible starting point. It encompasses a functional frontend, the central integration of product, inventory, customer, and order data via the JTL-WaWi, a basic customer account, a checkout with shipping and payment integration, and the handover of orders into the WaWi. In addition, the MVP enables the operation of multiple shops with market-specific settings and initial AI-assisted features for shop design.

For the implementation of the MVP, an ambitious realisation timeline of six to nine months is planned. This requires an interdisciplinary team comprising delivery, development, DevOps, quality engineering, product and project management, as well as UI/UX. Team capacities are oriented, depending on the scenario, to the reliable total technical effort and include an appropriate buffer for integration and project risks.

In this way, the MVP creates a solid foundation for the further development of JTL-Shop 6.0. The modular system architecture enables the structured addition of further functions and expansion stages, thus forming a production-ready and extendable starting point for continued scaling in national and international contexts. This enables the acquisition of new customers and the step-by-step migration of existing customers from the current shop concept.

## 2 Orientation within the Document
The document follows a structured approach from answering the "Why" through the "What" to the "How". It links market and competitive analyses with a clear positioning and derives from these the functional objectives as well as the corresponding technical, organisational, and operational implications.

|**Chapter**|**Contents**|
|---|---|
|Chapters 1 and 3|Scope and objectives of the engagement|
|Chapter 4|Market environment, relevant developments, and success logic|
|Chapter 5|Derivation of a positioning and implications for the JTL-Shop|
|Chapter 6|Guardrails and role model, functional and technical requirements as well as<br>platform and AI perspectives|
|Chapter 7|Technological requirements and architectural foundations|
|Chapter 8|Technical architecture: architecture principles, high-level and detailed<br>architecture description, as well as scalability|
|Chapter 9|Implementation steps for JTL-Shop 6.0 and|
|MVP Chapter 10|Conclusion|
|Appendix|Challenges, solution approaches, and supplementary directories|
|**Table 1 Chapter L**|**ogic**|

### Target-Group-Oriented Reading Recommendations
For executive management and leadership, it is recommended to start with Chapter 1 and Chapter 3, followed by Chapter 5 on positioning and Chapter 9 on MVP and follow-up releases, and Chapter 10 as the conclusion. For background on the derivation, Chapters 4 and 6 may be read as supplementary material as needed. For business and product roles, Chapters 4 through 6 are particularly relevant — that is, market and technology analysis, positioning, and functional and technical requirements. Chapter 9 is additionally relevant for contextualising the scope of the MVP and further development.

For architecture and development, Chapters 6 through 8 are relevant for requirements, architecture overview, and technical architecture. Chapter 9 supplements the implementation logic. For operations, infrastructure, and support, Chapters 7–9 are especially relevant, as they define architecture, operations, security, and scaling aspects as well as the concrete implementation steps. For sales, pre-sales, and customer success, Chapter 1 and Chapters 4 through 6 serve as a basis, particularly market and technology analysis, positioning, and requirements. Additionally, Chapter Error! Reference source not found. provides a reliable contextualisation of MVP and expansion stages.

For quick orientation, we recommend the following reading priorities:

|**Topic**<br>**Recommended Chapter**|
|---|
|Quick Overview<br>1 → 5 → 6 → 9 → 10|
|Decision Paper<br>1 → 3 → 4–5 → 9 → 10|
|Implementation Preparation (Technology/Operations) 6 → 7 → 8 → 9 → 10|
|**Table 2 Quick Reading Paths**|

## 3 Engagement
The software solutions of JTL-Software GmbH were originally developed for use in an on-premise environment. With more than 50,000 mail-order retailers using the full e-commerce portfolio including the merchandise management system JTL-WaWi, JTL is among the leading providers in the German-speaking market.

As part of the Cloud Journey initiative, JTL is developing the JTL-Cloud as a central platform that brings together retail, apps, and partners in a modern cloud environment. A core component is the JTL ERP Cloud as a SaaS ERP and cloud platform for e-commerce, available in the browser and centrally updated. The goal is to migrate the existing products into this platform model and modernise them technologically so that they can be operated in a permanently secure, flexibly extendable, and future-proof manner.

In this context, Coduct Solutions GmbH was commissioned to design a Minimum Viable Product (MVP) for a new, cloud-based JTL-Shop and to define the technical architecture. The MVP serves as the functional and technical foundation for the future JTL-Shop 6.0 and is intended to represent a future-proof vision of a JTL online shop for JTL retailers.

This document describes:

- the overarching target vision of the new JTL-Shop 6.0,

- the functional and strategic context of the new development

- as well as the technical architecture and implementation steps of an MVP.

### 3.1 Initial Situation and Motivation
The existing JTL-Shop 5.0 has grown historically as a strongly on-premise-oriented, deeply ERP-integrated shop system and is today operated primarily in conjunction with the JTL-WaWi. For many retailers, this close integration represents a significant advantage: product data, prices, stock levels, and orders are maintained centrally and consistently in a single leading system.

In day-to-day operations, however, it is increasingly apparent that the existing architecture model is reaching structural limits. Setting up and operating the shop requires extensive technical expertise as well as a deep understanding of the interplay between shop, WaWi, hosting, and extensions. Particularly smaller retailers who

"simply want to run a shop" quickly encounter high entry barriers and frequently depend on service partners — resulting in correspondingly higher time-to-market and rising total costs.

The current customer survey confirms this assessment: the perceived challenges lie less in individual missing features and more in the overall complexity of operations, the dependency on plugins and service providers, and the associated low time-tovalue. At the same time, the deep integration with the JTL-WaWi remains the central added value of the system. It is precisely this tension between strong process capability and significant entry barriers that makes clear that the shop must be reconceived at a structural level.

From a technical and operational perspective, further limitations are apparent. The current shop is operated predominantly in shared hosting environments, without automatic scaling, load balancing, or clean isolation of individual instances. Load peaks — such as at peak times like Black Friday — must be managed manually and, due to shared infrastructure, can affect multiple shops simultaneously.

An additional deficiency lies in the lack of an environment and lifecycle concept. The operation effectively knows only a single production environment. Development or

staging setups are not available as standard and are replaced, if at all, by manual workarounds. As a result, updates or plugin modifications frequently take place directly on the live system, which deters larger retailers in particular from using it. Extensibility is also limited by the existing architecture. The session-based checkout is difficult to customise and can only be extended by partners to a limited extent. APIs are only present in rudimentary form, which means that many extensions must intervene directly in the shop logic or compensate for missing WaWi interfaces as technical bridges. This leads to a heterogeneous ecosystem, complicates updates, and slows consistent further development.

From a product perspective, it is clear that Shop 5.0 is aimed primarily at technically proficient retailers and partners. While the system offers great freedom and customisability, it barely meets the requirements of those retailers for whom ease of use, standardised processes, and fast time-to-value are decisive. Compared to modern SaaS platforms, this creates a competitive disadvantage — despite the continued strong differentiation through the JTL-WaWi.

Against this background, the motivation for Shop 6.0 arises not solely from the migration to a cloud environment, but from the necessity of a structurally reconceived product: a scalable, operationally manageable platform that preserves the strengths of the WaWi while sustainably improving usability, extensibility, and economic operation.

The users of JTL-Shop 5.01 are predominantly small and medium-sized enterprises (SMEs) from the German-speaking region (DACH). Characteristic is a strongly operationally oriented use of the shop system, focused primarily on process stability, merchandise management integration, and efficiency in day-to-day business. The JTL-Shop is primarily understood and used as a frontend to the JTL-WaWi. Marketing, branding, or experience-driven use cases are of considerably less prominence.

#### Company Size and Structure
- Focus: small to medium-sized companies

- Common characteristics:

   - 1 to 50 employees

   - owner-managed or owner-led organisations

   - management operationally heavily involved

#### Assortment and Complexity
- Medium to large product catalogues

- on average several thousand items

- frequently five-digit SKU counts

- High functional complexity due to: `o` variant articles

   - tiered and customer group prices

   - `o` weight and shipping logic

   - B2B special cases

#### Industry Focus
• Classic retail (B2C)

> 1 Based on existing product strategies, Ideal Customer Profiles (ICPs), market analyses, and an extensive user survey provided by Cedric Fröhner.

- Pet supplies / pet market

- Sports and leisure goods

- Automotive parts and accessories

- Technical trade and wholesale

- Mixed B2C and B2B models

These industries are characterised by a broad product range and complex process requirements rather than strongly brand-driven sales logic.

The primary users of JTL-Shop 5.0 are:

- Managing directors / owners

- commercial roles

- E-commerce and operations managers

Characteristically, many of these users have no technical background. This results in:

- a high dependency on service partners

- intensive use of plugins and templates

- a pronounced need for stability, reliability, and clear structures

The decision in favour of JTL-Shop 5.0 is based, for the majority of users, on the following key arguments:

1. Seamless integration with the JTL-WaWi

   - The merchandise management system serves as the central system for items, prices, stock levels, and order processing.

2. Scalability for large assortments

3. Functional extensibility via plugins

4. German-speaking ecosystem

      - Community

      - Service partners

      - legal framework conditions (especially DACH)

In many cases, it is not the shop itself but the WaWi integration that represents the true added value of the overall system.

In operational use, the following patterns emerge:

- Heavily plugin-driven shops (payments, legal, marketing, search, design)

- High degree of customization, mostly implemented by service partners

- Cautious update strategies

   - Updates are frequently applied with delays

   - The primary reason is concern about incompatibilities with plugins

- Multi-shop functionalities are used, but perceived as complex, maintenance-intensive, and error-prone

#### Dominant user needs

- High stability and update reliability

- Ease of use, even without deep IT expertise

- Predictable and transparent costs

- Reliable core processes: order processing, shipping, payments, legal compliance

-

- Reduction of technical complexity

Currently of lesser relevance:

- Emotional branding

- Storytelling approaches

- Marketing automation

- D2C-typical experience features

- Highly modern UX concepts

### 3.2 Target vision
As context for the target vision, it must be taken into account that even in a modern cloud environment, seamless collaboration and communication between the individual system components — as previously in on-premise operations — remains guaranteed.

JTL-Shop 6.0 targets growth- and scale-oriented commercial enterprises that:

- serve multiple markets, brands, or channels,

- operate different business models (B2C/B2B) in parallel,

- expect ERP independence and integration capability,

- view commerce as a strategic growth driver.

#### User and company structure
|**Dimension**|**JTL-Shop 5.0 — current users**|**JTL-Shop 6.0 — strategic target**<br>**customers**|
|---|---|---|
|Company size|Small and medium-sized enterprises<br>(SMEs)|Medium to larger organizations|
|Organizational form|Often owner-managed, operationally<br>driven|Professionalized teams with clearly<br>defined roles|
|Decision structure|Owner- and risk-driven|Management- and ROI-driven|
|Market region|Focus DACH|DACH + European expansion|
|Growth ambition|Stabilization and efficiency|Scaling, internationalization|

**Table 3: User and company structure JTL-Shop 5.0 vs. 6.0**

#### Business model & market orientation
|**Dimension**|**JTL-Shop 5.0**|**JTL-Shop 6.0**|
|---|---|---|
|Business model|Predominantly B2C, partly hybrid B2B|Hybrid B2C/B2B, increasingly<br>enterprise B2B|
|Brand focus|Functional commerce|Brand and experience orientation|
|Internationalization|Low to moderate relevance|Core requirement|
|Multi-shop / Multi-<br>market|Present, but complex|Core component of the platform<br>strategy|

**Table 4: Business model & market orientation JTL-Shop 5.0 vs. 6.0**
#### Assortment & operational complexity
|**Dimension**|**JTL-Shop 5.0**|**JTL-Shop 6.0**|
|---|---|---|
|Assortment size|Medium to large|Large to very large|
|Variants & pricing logic|Strongly pronounced|Highly differentiated|

|Process focus|Order and goods flow|End-to-end commerce orchestration|
|---|---|---|
|Scalability|Technically possible, organizationally<br>limited|Structurally intended|

**Table 5: Assortment & operational complexity JTL-Shop 5.0 vs. 6.0**
#### Technological orientation
|**Dimension**|**JTL-Shop 5.0**|**JTL-Shop 6.0**|
|---|---|---|
|System understanding|Shop as frontend to the WaWi|Shop as central commerce platform|
|ERP dependency|Strong (JTL-WaWi as core)|ERP-agnostic|
|Extensibility|Plugin-centric|API-first, modular|
|Architecture|Predominantly monolithic|Cloud-native, scalable|
|Operating model|Self-hosted /partner-operated|SaaS / Managed Platform|

**Table 6: Technological orientation JTL-Shop 5.0 vs. 6.0**
#### User expectations & priorities
|**Dimension**|**JTL-Shop 5.0**|**JTL-Shop 6.0**|
|---|---|---|
|Stability priority|Very high|High, but not solely dominant|
|Openness to<br>innovation|Low to moderate|High|
|UX & design|Secondary|Strategic differentiator|
|Automation|Functionally limited|Core expectation|
|Data & analytics|Used operationally|Strategically decision-relevant|

**Table 7: User expectations & priorities JTL-Shop 5.0 vs. 6.0**
#### Role of partners
|**Dimension**|**JTL-Shop 5.0**|**JTL-Shop 6.0**|
|---|---|---|
|Partner dependency|High (implementation &<br>operations)|Strategic (integration & scaling)|
|Partner role|Problem-solver & operator|Enablement &growth partner|
|Merchant autonomy|Low to medium|Medium to high|

**Table 8: Role of partners in JTL-Shop 5.0 vs. 6.0**

The new shop will be provided as Software-as-a-Service (SaaS) and continues to use JTL-WaWi as the leading ERP system and central data source. At the start of the project, it may be necessary for JTL-WaWi to still be operated in an on-premise environment. The system architecture is therefore designed so that both on-premise and future cloud-based variants of the WaWi can be connected — without modifications to the frontend or the middleware. AI is defined in the target vision as a functional platform capability that builds on consistent data and clear process ownership to support merchants in operations and optimization using a data-driven approach. The shop is aligned so that future agent-based interaction patterns can be supported via structured data and status models.

The shop frontends will be fully decoupled and developed as independent headless frontends. Through the use of modern web and PWA concepts as well as a modular architecture, a high degree of flexibility, multi-store capability, and reusability is achieved.

The technical implementation is based on the Microsoft Azure cloud platform. This fulfills key requirements of modern cloud infrastructures: automatic, demand-driven resource allocation (autoscaling), high availability, and horizontal and vertical scalability. The architecture is extensible so that it meets the requirements of both an MVP and subsequent production-scale deployment.

The target vision therefore encompasses:

- a fully cloud-native multi-shop platform with central ERP integration (JTL-WaWi),

- a decoupled, API-first architecture with an independently developed headless frontend,

- an Azure-based infrastructure with a focus on scalability, high availability, and automation,

- support for both on-premise and future cloud-based JTL-WaWi instances,

- a modular, extensible solution that flexibly supports future requirements and integrations,

- as well as a stable and maintainable technical foundation for the long-term further development of the JTL-Shop ecosystem.

This target vision serves as the strategic reference framework for the implementation of the MVP and the subsequent development of JTL-Shop 6.0.

## 4 Market and technology analysis
The DACH market for e-commerce platforms is undergoing comprehensive modernization, driven by higher customer expectations, increasing complexity of business processes, and advancing technological developments.

This chapter provides a structured overview of the most important market trends, technological developments, and competitive dynamics. The aim is to understand the framework conditions that shape the requirements of modern commerce systems and to derive from these the strategic implications for the development of JTL-Shop 6.0.

### 4.1 Technological development in e-commerce
The technological development in e-commerce is moving away from monolithic, function-centric shop systems toward modular, cloud-native platform architectures. This shift is less the result of individual innovations and more a structural response to changed market requirements.

Merchants today operate in an environment characterized by a multitude of sales channels, short innovation cycles, increasing integration requirements, and growing expectations regarding performance and user experience. Commerce systems are therefore no longer isolated applications for order processing, but integral components of distributed, highly integrated system landscapes.

Architectural decisions have a decisive influence on the flexibility, scalability, and future-readiness of a commerce platform. They enable operators to respond dynamically to market changes and to adapt the platform efficiently to their needs.

#### 4.1.1 Architecture paradigms: Composable Platform
The evolution of e-commerce architectures can be described in several successive paradigms, each placing different emphases on flexibility, extensibility, and operating model.

In the early phase, monolithic systems dominated, in which frontend, backend, and business logic were tightly intertwined. Extensions frequently required interventions in the system core, leading to high complexity, long release cycles, and rising maintenance costs.2

With the increasing adoption of APIs and modern web technologies, the headless paradigm gradually established itself. Frontend and backend were decoupled, enabling user interfaces to be developed and operated independently of the underlying commerce logic. This separation allowed significantly greater creative freedom, better performance optimization, and the parallel use of multiple touchpoints such as web, mobile, or POS.

In recent years, composable commerce architectures have emerged. These follow the principle of providing individual functionalities as independent, specialized services that communicate with one another via clearly defined interfaces. Microservices, API-first design, cloud-native operations, and high interchangeability of individual components form the foundation. The aim is a flexibly composable system that can continuously adapt to new requirements. This development increases technical complexity at the

> 2 (Dragoni et al., 2017)

architecture level, but creates the prerequisite for greater adaptability and speed of innovation. This represents a decisive advantage particularly for merchants with growing system landscapes and differentiated business models.

To condense this line of development, the following table summarizes the most important architecture paradigms in e-commerce.

AI-assisted commerce is to be classified as a capability and interaction layer that builds on top of these architectures. While Composable / MACH creates the structural foundation (API-first, clearly delineated services, cloud-native operating models), AI-assisted commerce extends the platform with context-based support along discovery and process chains. This includes in particular intelligent search and ranking mechanisms, personalized content delivery, and assistance functions that prepare decisions and support operational workflows.

For modern platforms, it is crucial that the AI layer is connected via stable, machine-readable data and unambiguous process states. The more consistently product data, pricing and availability information, variant logic, and order and payment status are structured and made available, the more AI can generate content and provide live inprocess support (up to interaction patterns in which the actual customer interaction can partially detach from the classic shop interface).

|**Period**|**Paradigm **|**Characteristics**|**Examples**|
|---|---|---|---|
|**2010–2015**|<sup>Monolithic</sup><br>systems|Tight coupling, limited extensibility,<br>core modifications|Magento, Shopware 4|
|**2015–2020**|Headless Commerce|Separation of frontend and backend,<br>REST/GraphQL APIs as standard|Shopify APIs,<br>Shopware 6 Store API|
|**2020–2026**|<sup>Composable</sup><br>Commerce /<br>MACH|Microservices, API-first, cloud-native,<br>frontend-agnostic|Commercetools,<br>Spryker|
|**2024–2026**|<sup>AI-assisted</sup><br>Commerce|AI-based personalization, automated<br>content,intelligent search|Shopify Magic,<br>Commercetools AI|
|**Table 9: Evol**|**ution of e-commerce a**|**rchitectures**||

The time periods in Table 5 are therefore overlapping. Composable/MACH describes the architectural foundation that continues to establish itself more broadly, while AI-assisted commerce becomes visible from 2024 onward as an additional dimension of evolution.

#### 4.1.2 Frontend technologies: Modular Storefront
Classic, template-based shop systems with tightly coupled presentation and business logic are increasingly being replaced by independent storefront applications that operate independently of the chosen backend solutions. This decoupling allows interaction layers to be designed flexibly, different target groups and channels to be addressed in a differentiated manner, and user experiences to be optimized specifically without changing the underlying process logic.

Interaction layers encompass website, mobile, POS, and marketplace UI, as well as the channel- and target-group-specific delivery of frontends. Only through a separation of concerns is it possible to manage this multitude of interaction layers without affecting the core processes.

Modular storefront architectures are typically based on established web frameworks and communicate with the operational core via interfaces.

As a result, the frontend becomes an independent yet integrated interaction layer within the overall architecture. As the system landscape grows — for example through additional services, data sources, or specialized backend components — the storefront can be extended via existing APIs without itself needing to be fundamentally replaced. New functions are created through integration, not through structural reimplementation.

The frontend becomes a central but deliberately decoupled building block of a scalable commerce architecture: flexible at the surface, stable in the process and data logic.3

#### 4.1.3 Integration and data architectures: Orchestration
With the increasing modularization of commerce platforms, the requirements for integration and data architectures are changing fundamentally. While classic e-commerce systems frequently relied on periodic synchronization mechanisms between individual applications, event-driven and orchestrating approaches are now moving to the forefront. The aim is to make data available and controllable across systems in near real time.

E-commerce platforms are in constant interaction with inventory management systems, logistics solutions, marketing and CRM systems, marketplaces, and specialized domain systems. In this environment, the shop loses its role as the sole data holder and becomes a controlling node within a distributed system network. Integration therefore no longer means only data transfer, but the targeted orchestration of processes across system boundaries. A key prerequisite for successful integration is architectural discipline:

- clearly defined system ownership,

- consistent data models,

- transparent process states,

- clearly structured interfaces,

- real-time or near-real-time data availability.

This foundation enables the use of event-driven integration patterns (e.g. pub/sub, event streaming). Events such as changes to products, prices, inventory, or order status are processed as individual events and forwarded to relevant systems. This increases responsiveness, reduces integration errors, and creates the basis for consistent management across multiple channels.4

With the growing number of external touchpoints — for example through social commerce formats — requirements increase further. Prices, inventory levels, and product information must be available consistently across channels, while orders must be reliably transferred into existing fulfillment and accounting processes. Structural separation is the prerequisite for data-based control mechanisms. E-commerce platforms are evolving into systems that prepare decisions or support them in a context-dependent manner — for example in pricing logic, inventory management, or cross-channel orchestration.

> 3 (Tiwana, 2013)

> 4 (Verhoef et al., 2015)

#### 4.1.4 Cloud-native operations and scalability
A further trend is the shift to cloud-native operating models. These enable flexible scaling of resources, automated deployment processes, and higher availability compared to classic on-premise installations. Cloud-native architectures are designed to dynamically absorb traffic peaks and continuously roll out new functionalities without disrupting ongoing operations.

For retailers, this means a significant reduction in operational risks as well as improved predictability of costs and resources. At the same time, the focus shifts away from infrastructure-related issues toward specialist and strategic topics. The technical platform is thus increasingly becoming an enabler that allows for innovation rather than constraining it through rigid operating models.

Cloud-native concepts only deliver their full benefits when built on a suitable architecture and integration strategy. A consistent evolution toward modular, API-based approaches is therefore critical.

#### 4.1.5 Agentic Shopping & AI in Commerce
With the growing prevalence of generative AI systems, the topic of agentic commerce — that is, agent-based purchasing — is also gaining importance. This refers to systems in which purchasing decisions are made through dialogue-based interaction with an intelligent system that researches, evaluates, and, where applicable, prepares or executes transactions. Unlike classical commerce platforms, this model shifts the primary point of interaction away from the shop into an upstream assistance layer. The user articulates their request in natural language; the system aggregates available offers and presents a curated selection. The actual shop becomes, in this scenario, a connected data and transaction source.

Comparison portals, specialized marketplaces, and channel-bound assistants have already pursued similar objectives: reducing complexity through pre-selection and aggregation. However, their market penetration has in many cases remained limited to specific segments. The causes lay less in technical inadequacy than in structural factors such as a limited data base, restricted supplier diversity, lack of neutrality, or insufficient user acceptance.

AI agent systems face comparable challenges. Their performance depends significantly on the quality, timeliness, and completeness of the underlying data. There is also the question of transparency and traceability of recommendations, particularly in commercial contexts where the economic interests of agent operators play a role.

At the same time, it cannot be assumed that dialogue-based shopping assistance will fully replace the fundamental need for direct interaction with brands, products, and shops. The traditional shop continues to fulfil functions that go beyond pure product selection: brand building, presentation, trust, consultation, inspiration, and differentiation. These elements can only be reproduced to a limited extent in aggregating or agent-based models.

Alongside dialogue-based assistance systems, AI-supported functions are increasingly being established that unlock economic efficiency gains and revenue potential across the entire customer journey.

AI support offers in particular:

- the automated creation of product descriptions and marketing copy based on generative language models,

- AI-assisted generation and editing of product images (e.g. through automatic background removal or scene-based visualization via text input),

- personalized product recommendations and dynamic assortment logic based on real-time behavior and customer segmentation,

- as well as AI-based chatbots that not only answer support inquiries but are increasingly also acting as contextual sales assistants.

These functions enable a significant reduction in manual effort (e.g. in content creation), higher conversion through personalized outreach, and an improved time-tomarket with simultaneous cost control. Commerce platforms thereby create the foundation for an economically scalable retail architecture.

### 4.2 Market Structure and Key Vendor Groups
The e-commerce platform market in the DACH region is characterized by high diversification and can be divided into four distinct vendor segments. These clusters differ in their fundamental technological orientation, their underlying operating models, and in the way they integrate commerce into existing system landscapes. They thus form the structural framework within which competition, product strategies, and technological developments in the market unfold.

The market structure shows that vendors differentiate themselves not solely through sheer breadth of functionality, but through their underlying architecture and operating model, their integration capability, and their compatibility within existing system landscapes and organizational structures. The systemic classification serves as an analytical basis for examining specific market participants and their respective characteristics along these dimensions. The relevant shop vendors in the DACH region are categorized in the following table according to their characteristic attributes as well as their respective strengths and weaknesses.

|**Category**|**Characteristics**|**Strengths**|**Weaknesses**|
|---|---|---|---|
|**Global SaaS**<br>**Market**<br>**Leaders**|Cloud-native, high degree of<br>automation, globally scalable|Largest ecosystem,<br>excellent developer<br>experience, high<br>scalability|Limited DACH<br>specialization|
|**Regional**<br>**Champions**|German focus, hybrid<br>models, strong B2B<br>capabilities|Deep localization,<br>strong partner<br>network|Reduced scalability in an<br>international context|
|**Enterprise**<br>**Composable**<br>**Vendors**|MACH architecture, API-<br>First, individual<br>composability|Maximum flexibility,<br>enterprise-ready|Very high costs & project<br>complexity|
|**Plugin-/Open-**<br>**Source-based**<br>**Systems**|Self-/partner-operated,<br>theme/plugin-driven,<br>strongly tied to ecosystem|High configurability,<br>low barrier to entry,<br>wide range of exten-<br>sions|Higher operational and<br>integration effort,<br>quality/governance risks in<br>the exten-<br>sion stack|

**Table 10: Vendor clusters in the DACH region**

Examining specific market participants shows that identical architectural paradigms — such as API-First or Headless — are used in practice in very different ways. While some vendors use these concepts primarily for functional extensibility within existing platform boundaries, others use them as the foundation for fully modular, service oriented system landscapes. Plugin- and open-source-based systems represent a distinct logic of their own, in which extensibility is organized less through platform boundaries and app ecosystems than through the software core, themes, and plugins.

The differences between systems should not be understood as linear stages of development, but as parallel models addressing different retailer realities. The competitive landscape is therefore shaped less by direct feature comparisons than by structural decisions around architecture, integration depth, and operating model. For a compact overview, the vendors examined and their key classification criteria are summarized in the table below.

|**Vendor**|**Target Group**|**Architecture Model**|**Key Characteristics**|
|---|---|---|---|
|**Shopify**|SMB →<br>Enterprise|SaaS, Headless|Largest<br>app<br>ecosystem,<br>best<br>developer experience (DX), strong<br>automation|
|**Shopware**|Mid-Market →<br>Enterprise|API-First, Hybrid (SaaS<br>+ Self-Hosted)|<br>Strong B2B features, Flow Builder<br>(no-code process automation),<br>German localization|
|**WooCommerce**|SMEs,<br>WordPress<br>users|Plugin-based|Low barrier to entry, vast<br>WordPress ecosystem|
|**Commercetools**|Enterprise|MACH|100% composable, globally scalable|
|**Spryker**|Enterprise, B2B<br>& Marketplaces|<sup>MACH</sup>|High modularity, Marketplace Suite|
|**BigCommerce**|Mid-Market →<br>Enterprise|SaaS|Native Multi-Storefront, 0% transaction<br>fees|
|**Plentymarkets**|Mid-Market|Monolith(ERP+Shop)|Strong marketplace capability|
|**PrestaShop**|SME → Mid-<br>Market|Open Source, modular<br>(Modules/Themes)|Strong module ecosystem, widespread<br>in EU,no SaaS offering|
|**Magento/ Adobe**<br>**Commerce**|Mid-Market →<br>Enterprise|Open Source, modular<br>(Framework/Extension<br>s)|High degree of customizability and,<br>as a result, high implementation,<br>integration,and operational effort|

**Table 11: Competitive landscape at a glance**

#### 4.2.1 Global SaaS Market Leaders
Global SaaS platforms such as Shopify and BigCommerce consistently rely on cloud-native and API-oriented architecture. Core commerce functions are offered as managed services and bundled within a centralized operating model. Extensions are delivered via app ecosystems and external integrations, with business logic remaining largely within defined platform boundaries. Custom adaptations and complex process logic are typically implemented through additional services outside the core system.

In day-to-day operations, the e-commerce frontend, platform core, and external specialist systems are kept separate from one another. Inventory management, fulfillment, or specific pricing and process logic are connected via integrations and are not part of the platform core. The resulting operating model is highly scalable, but remains deliberately abstracted and offers only limited options for deep-level customization.

##### 4.2.1.1 Shopify (SaaS) Strategic Positioning
Shopify is a highly standardized SaaS platform with rapid scalability and international applicability. The platform reduces the operational burden on retailers by largely taking over hosting, security, updates, and platform operations. Extensions are made primarily via APIs and a large ecosystem, through which additional functionality can be added within a clearly framed platform model.

###### Strong App Ecosystem and Low Time to Market
Shopify impresses with a large app marketplace and numerous interfaces. Retailers can quickly select and integrate extensions for marketing, analytics, logistics, and payments, enabling shops to launch swiftly and be expanded incrementally. The cost of this model lies primarily in licensing, app, and transaction and payment fees, as well as in the growing dependency on external extensions and integrations.

###### AI Features and AI-First Approach in SaaS Commerce
Shopify positions AI visibly as an integral part of its product and pursues an AI-First orientation. With Shopify Magic and Sidekick, native AI features are available that support content creation and operational tasks in the admin area. Furthermore, AI is increasingly being integrated into storefront features, and Shopify is addressing agent-based commerce scenarios as a potential future sales channel.

###### No Multi-Shop and ERP Integration via Workarounds
Shopify does not offer a direct multi-shop solution. Each store runs independently, and even with centralized management the backends remain separate. Shopify also has no ERP system of its own; integration is achieved via apps and connectors and is limited in depth and controllability by platform boundaries and API limits. For complex process and integration scenarios, this creates additional effort in integration, middleware, and operational management.

###### Assessment
Shopify stands for standardization, speed, and efficient SaaS operations. However, as process and integration complexity grows, key challenges shift to the integration and governance layer outside the platform.

##### 4.2.1.2 BigCommerce (SaaS) — Strategic Positioning
BigCommerce is a SaaS commerce platform with rapid activation and good scalability. Unlike all-in-one systems, BigCommerce pursues an API-oriented Open SaaS approach that specifically supports integrations and extensions. The platform targets organizations that want to leverage SaaS benefits without fully sacrificing integration capability and individual customization, positioning itself between standard solutions and bespoke enterprise architectures.

###### Native Multi-Storefront Capability and API Orientation
BigCommerce offers a native multi-storefront feature in which multiple storefronts are operated via a shared backend, and central master data and

transactions can be managed consistently. Each storefront can be individually configured and operated with its own domain, supporting multi-brand and multi-shop scenarios.

The practical suitability depends, however, on the required degree of separation. Where hard tenant isolation with full autonomy for individual shops is required, additional architectural measures or separate instances may become necessary. ERP systems are integrated via apps, standardized connectors, or APIs. Standard processes can be mapped well, while platform restrictions, API limits, and the prescribed data and process model limit the depth of individual customization. For complex requirements — such as specific state models or tenant-specific process variants — additional integration and middleware effort is incurred outside the platform.

###### Open AI Integration and Modular BigAI Features
In the area of AI, BigCommerce deliberately positions itself as open. AI is bundled under the term BigAI and understood as a combinable capability, consisting of proprietary building blocks (e.g. Copywriter, Predictive Analytics, recommendations in future) as well as partner solutions and external services via APIs. This creates less a closed native AI suite than an extensible modular system.

BigCommerce also addresses agent-based commerce scenarios and unified commerce platforms (UCP) as potential interaction and access channels, which is particularly attractive for integration-oriented organizations that wish to assemble AI functionality from multiple components.

###### Platform Limits in ERP Orchestration and Tenant Separation
Despite multi-storefront capability, BigCommerce remains a controlled SaaS system. Deep, individually controllable ERP orchestration lies primarily outside the platform and must be secured via integration, middleware, and architectural guardrails when high consistency and control are required.

SaaS operations are, in return, straightforward, as hosting, updates, and security are handled by the vendor. Effort and costs arise primarily from licenses, apps, and the required integration and customization work, particularly in ERP-heavy or highly variant-rich scenarios.

###### Assessment
BigCommerce offers a stable SaaS platform with multi-storefront capability and strong API extensibility. The platform is particularly well-suited for multiple shops or brands with shared processes and a preference for SaaS operations. Where there is high process variance, deep ERP orchestration, or hard tenant separation, the effort shifts to the integration and architecture layer outside the platform.

#### 4.2.2 Regional Champions
Regional platform vendors in the DACH region, such as Shopware and Plentymarkets, are closely aligned with the requirements of the German-speaking retail market. Their solutions take into account specific regulatory, tax-related, and procedural requirements, and integrate online shops, marketplace connections, and operational retail processes more deeply than globally standardized SaaS platforms.

Technologically, these vendors rely on a combination of modern API-based concepts and established system components. Headless and integration approaches are being incorporated incrementally, resulting in a hybrid model between stability and modernization. The platforms are typically deeply embedded in retail and fulfillment processes, and in addition to standard shop functions they take on supplementary tasks such as marketplace management, process automation, and cross-channel data consistency. The degree of modularity and technical decoupling remains below the level of composable enterprise architectures.

##### 4.2.2.1 Shopware 6 (Open Source / PaaS) — Strategic Positioning
Shopware 6 is a leading commerce vendor in the DACH region, targeting in particular the mid-market through to large enterprises. The platform offers greater flexibility and customization than classic SaaS solutions while also being strongly aligned with the legal and tax requirements of the German-speaking market. Shopware pursues a hybrid strategy combining open source, self-hosted, and PaaS deployment, thereby enabling greater control and adaptability than highly standardized platform models.

###### Native Multi-Shop Capabilities and High Customizability
Shopware natively supports multi-shop scenarios through the concept of sales channels. Within a single installation, multiple shops, brands, or channels can be mapped organizationally, with varying degrees of separation and reusability depending on the target architecture.

The platform can be flexibly integrated with external inventory management and process systems, typically via established integrations, connectors, or custom interfaces. Compared to standardized SaaS platforms, Shopware offers greater openness for individual data and process models. Extensions are delivered through a plugin ecosystem as well as through custom adaptations within the platform architecture; headless and API-first concepts are available and can be consistently leveraged depending on the project focus.

###### AI as an Integrated Copilot for Content, Product Data, and Operations
Shopware has clearly positioned AI as a core product component, bundling the relevant features under Shopware AI and the AI Copilot respectively. Unlike many platforms, Shopware goes beyond pure text generation and addresses several operational use cases directly within the admin area, including content for experience worlds, image keywording, product attributes, review summaries, translations, and contextual search and assistant functions. Strategically, Shopware communicates this in the direction of agent-based commerce scenarios and positions the Copilot as an embedded support tool for product, content, and operations tasks in the backend.

###### Governance and Operations: Flexibility Demands Discipline
Shopware offers a high degree of flexibility but comes with typical governance requirements, particularly regarding plugin quality, updates, security, and long-term maintainability. Without controlled extension and clear guardrails, increasing complexity can give rise to redundancies, inconsistent data models, and high maintenance custom solutions. Since Shopware does not include its own ERP system, integration and process consistency depend heavily on architecture and maintenance; particularly in

ERP-centric applications, a clear role model is required. In operations, Shopware enables more control than SaaS solutions but requires correspondingly greater self responsibility for updates, performance, and security. Costs arise primarily from projects, integrations, and ongoing governance rather than from licenses.

###### Classification
Shopware combines standardization for the DACH market with high flexibility and native multi-shop support. For merchants with specific processes it is a powerful platform, but it demands architectural discipline and operational maturity.

##### 4.2.2.2 Plentymarkets / PlentyONE Strategic Positioning
PlentyONE is a regional platform provider that goes beyond a classic shop system. The solution bundles shop, ERP and inventory management, and multichannel functions in a central suite, enabling trading processes, channels, and operational workflows to be managed from a single system — from product data and stock levels through to order processing and fulfillment. This suite approach enables rapid implementation and close process alignment, but requires a clear positioning of PlentyONE within the overall architecture.

###### Integrated Trade Processes, Multichannel Focus, and Suite Logic
PlentyONE supports multi-shop and multichannel scenarios directly within the platform, with the primary focus typically on channel-based management, for example for own shops and marketplaces. Storefront components configured in the backend are available for the online shop. The shop is not an independent product but part of the suite, tightly coupled to the backend, which allows central processes to be mapped within a single system. Extensions are possible via plugins, marketplace, and interfaces, but require clear guardrails defining which logic remains in the core system and what is added through integrations.

###### Focus on Process Integration Rather Than a Clear AI-First Positioning
In the area of AI, PlentyONE is currently less clearly positioned than some competitors. The platform primarily communicates its focus as an all-in-one e-commerce ERP and multichannel system; the foreground emphasis is on process integration, automation, channel management, and operational platform operations. AI-adjacent use cases do exist but currently appear predominantly through marketplace plugins and partner solutions, for example for content generation, personalization, or pricing and repricing.

In parallel, PlentyONE is modernizing its storefront toward PWA-capable, high-performance web app frontends. This improves load times and mobile experience and fundamentally creates a better foundation for personalized and AI-adjacent interaction scenarios, without PlentyONE currently communicating a clearly developed native AI suite or AI-first strategy.

###### Tight Coupling of Shop and ERP Logic as well as Role Ambiguity
A central challenge lies in the tight coupling of the shop layer and ERP or inventory management logic. In more complex system landscapes this quickly leads to overlaps in data and process ownership, particularly

when PlentyONE is used simultaneously as an operational hub and additional leading systems are in use.

PlentyONE can serve either as the central system for data and process ownership or as a commerce and channel layer within a modular landscape. If the latter is chosen, relevant master and transactional data must be consistently available in PlentyONE for shop and channel processes to run reliably. Without a clear division of roles, duplicate maintenance, unclear states, and parallel process logic arise. As customization increases, governance effort also grows, particularly with regard to extensions, updates, compatibility, and maintainability.

###### Classification
PlentyONE accelerates commerce and trade processes through an integrated suite and offers high efficiency in a multichannel context. At the same time, the tight coupling reduces the degree of decoupling, which is why a strategic positioning within the system architecture is critical. For organizations with all-in-one requirements, PlentyONE is well suited as a central commerce hub, whereas in modular landscapes the effort for data ownership, integration, and governance increases significantly.

#### 4.2.3 Enterprise Composable Providers
Enterprise composable commerce platforms are based on modular architectural principles such as microservices, API-first, and headless concepts. Commerce is understood as a flexibly composable system consisting of specialized services orchestrated through defined interfaces. Platforms such as Commercetools and Spryker break completely with classical shop systems and provide a technological foundation on which individual system landscapes are built.

The implementation of modern architectural trends such as event-driven architecture and cloud-native operations is central. The platform does not provide a fixed feature set; instead, it enables organizations to design and extend commerce solutions according to their own requirements.

This model demands a high level of technical and organizational competence from users. Integration, extension, and operations are implemented under self responsibility, leading to increased project complexity and longer implementation cycles.

##### 4.2.3.1 Spryker Strategic Positioning
Spryker addresses enterprises with complex business models and a high need for individual process and integration logic. The platform is headless, API-first, and modular in structure, enabling sophisticated commerce and transaction scenarios to be mapped flexibly. The focus is less on a rapid standard go-live and more on embedding commerce as part of a comprehensive digital business architecture.

###### Composable Architecture and Process Adaptability
Through its strictly modular structure, functions, services, and domain logic can be flexibly combined and deeply integrated into existing IT systems. This makes Spryker particularly well suited for complex B2B processes, industry-specific models, or differentiated pricing and customer logic. Implementation does, however, require a clear target vision and disciplined integration and architecture work.

###### AI in the Composable Context
Spryker does not provide AI as a closed product suite but as extensible platform logic. The value arises from structural openness: data, processes, and logic can be organized so that external AI services or assistant systems are connected consistently. This makes Spryker particularly suitable for organizations that think of AI as part of a broader platform strategy.

###### High Degrees of Freedom and High Governance Effort
The high degree of flexibility demands consistent architectural decisions, governance, and an experienced delivery setup. Without clear guardrails, complex and difficult-to-maintain system landscapes with high project dependency emerge. The effort therefore lies less in licenses and more in architecture, integration, and operations.

###### Classification
Spryker is a powerful composable enterprise platform for companies with complex business models and high organizational maturity. The platform is particularly suitable when commerce must be deeply embedded in individual process and system landscapes and high degrees of freedom are strategically desired. Spryker stands for high flexibility and integration capability, but comes with significantly higher architecture, governance, and operational effort.

##### 4.2.3.2 Commercetools Strategic Positioning
Commercetools is one of the defining providers in the composable commerce space and positions itself clearly through MACH architecture, API-first, cloud-native, and headless. The platform targets enterprise organizations that understand commerce as a modularly composable system landscape and require maximum freedom for frontend, services, and integrations. Rather than a pre-shaped shop core, Commercetools delivers a commerce-specific infrastructure on whose basis companies can individually design their target architecture.

###### MACH Architecture, API-First, and Integration Capability
The strength of Commercetools lies in its consistent API-first architecture. Commerce functions are provided as flexibly consumable services and can be combined with frontends, middleware, PIM, ERP, search, or experience components. In international and differentiated commerce scenarios in particular, this creates significant degrees of freedom: data models, customer journeys, and cross-channel orchestration do not have to be conceived within a monolithic system. Multi-shop, omnichannel, and brand-specific architectures can be mapped well, provided the organization is willing to actively shape the resulting system landscape and operate it long term.

###### AI-First and Agentic Commerce as a Development Path
Commercetools is increasingly betting on AI-first commerce and agentic commerce. AI is understood not merely as a feature extension but as the next evolutionary stage of commerce infrastructure. The prerequisite for this is composable, API-oriented, and machine-readable commerce models that make it possible to productively integrate external AI systems, agents, or new interaction forms. Commercetools thereby addresses in particular organizations that already think of commerce as AIready infrastructure today and are systematically preparing for future agentic channels.

###### Maximum Flexibility with High Architectural Responsibility
The platform's high openness goes hand in hand with significant architecture and delivery effort. Commercetools does not offer a "ready-made" shop product; instead, it requires clear decisions in areas such as frontend, search, content, middleware, operations, observability, and governance. This freedom makes the platform attractive for complex enterprise landscapes but simultaneously raises the demands on target architecture, organizational maturity, and a robust integration model. Without clear responsibilities and structured architecture and operations design, the system landscape can quickly become costly, fragmented, or difficult to govern.

###### Classification
Commercetools is prototypical of the enterprise composable segment: maximum flexibility, high integration capability, and strong suitability for international, complex, and long-term individualized commerce landscapes. The platform is most beneficial when organizations deliberately want to design a modular target architecture and possess the necessary governance and delivery maturity.

#### 4.2.4 Plugin- / Open-Source-Based Systems
Plugin- and open-source-based commerce systems form a distinct category in the market, characterized by an extensible software core. Functionality and design are built out primarily through themes, plugins, and community extensions, enabling flexible adaptation to individual requirements. In contrast to SaaS platforms, responsibility for operations, scaling, and maintenance lies largely with the merchant or their service providers.

Examples such as WooCommerce, integrated into the WordPress ecosystem, as well as PrestaShop and Magento Open Source illustrate the diversity of this model. PrestaShop relies on a module system and is particularly widespread in the European SME market, while Magento Open Source serves as the base version for more sophisticated, custom-developed shops. The efficiency of these systems depends heavily on hosting, the extension stack, and implementation quality, which entails both greater design freedom and a higher need for technical expertise. With these systems, project and operational responsibility lies more heavily on the merchant or agency side. Scalability, performance, and security are determined primarily by the quality of the extensions used and the integration logic. In the right market segment these platforms offer flexible application possibilities, but differ from centrally managed platform models in terms of cost structure and governance.

##### 4.2.4.1 Magento 2 / Adobe Commerce (Open Source / SaaS / PaaS) Strategic Positioning
Magento 2 is the open-source foundation and forms the technical basis of the platform. Adobe Commerce extends Magento 2 with enterprise features, support, and deep integration into the Adobe Experience Cloud. Both are based on the same framework but differ in license, feature scope, and the connection to the Adobe ecosystem.

Magento and Adobe Commerce respectively are typically used when complex commerce requirements, extensive catalogs, international deployments, or demanding multi-shop scenarios are needed. The platform offers high degrees of freedom but requires technical and organizational maturity and is usually individually configured within the scope of an implementation project. Magento is therefore less a standard product and more a deliberately chosen architecture and platform decision. **Native Multi-Shop Capability and Maximum Customizability** Magento offers strong multi-shop functionality: multiple websites, shops, and views can be managed flexibly within a single installation, including separate brands, domains, and assortments. A clearly planned multi-shop concept is critical for maintaining manageable structures, as without it a lack of clarity and high maintenance effort can quickly arise.

The platform is designed to integrate into existing system landscapes. ERP integration is typically achieved through APIs, middleware, and a project-specific integration design. The central advantage lies in the high degree of controllability: data models, process logic, and interfaces can be deeply adapted to individual requirements.

###### AI-powered experience for personalization, search and merchandising
Through its embedding in the Adobe Experience Cloud, Adobe Commerce occupies a distinctive position in the field of AI, particularly for personalization, search and merchandising. With AI-based recommendations, Live Search and intelligent reranking, the focus is on conversion, discovery and personalization at scale. Of strategic relevance is the fact that AI is not conceived in isolation within commerce, but as part of a comprehensive data and marketing architecture — for example via Customer Data Platform, analytics and journey orchestration. Adobe Commerce plays to its strengths especially when AI is to be deployed as an enterprise-wide experience and personalization capability.

###### High complexity as well as governance and operational overhead
The high degree of flexibility demands strict architectural discipline and careful governance. Without clear guardrails, redundant logic, inconsistent states and hardto-maintain custom solutions emerge quickly — particularly in multi-shop setups, individual catalog logic and special-case processes.

Extensions and partner solutions enable a broad functional range, but increase requirements for quality management, test automation, and patching and upgrade processes. Operations, hosting, scaling and security also require corresponding expertise. The main costs therefore typically arise from implementation, integration and ongoing operations rather than from licensing.

###### Classification
Magento 2 and Adobe Commerce respectively offer multi-shop capability, high adaptability and flexible integration, and are suited to complex international commerce scenarios with a high degree of customization. At the same time, the organizational and technical overhead increases considerably, which is why the platform is primarily suited to organizations with clear governance, architectural discipline and corresponding operational maturity.

##### 4.2.4.2 WooCommerce (plugin-/open-source-based) — Strategic positioning
WooCommerce is a WordPress-based shop system used primarily on content oriented websites in the SMB and lower mid-market segments. It excels through low barriers to entry, rapid availability and a broad plugin ecosystem. Rather than a rigidly defined platform logic, WooCommerce offers a modular building-block approach, while operations, scaling and governance largely rest with the merchant or partner.

###### High flexibility through the plugin ecosystem and low barrier to entry
The large plugin ecosystem enables rapid customization for simple to moderately complex requirements and is particularly well suited to content-adjacent commerce solutions. As process and integration complexity grows, however, the central challenges shift toward governance of the plugin stack as well as operations, quality assurance and upgrade capability. The more tightly integration logic and stability must be secured through extensions and additional services, the more WooCommerce evolves from a building-block toolkit into a project-specific solution.

###### Flexible AI building blocks rather than a native AI platform
AI features in WooCommerce are mostly available via extensions, marketplace solutions or external services — not as a core platform function. AI plugins exist for product copy, assistants, recommendations and automated content creation, though quality and maintainability vary considerably. With its MCP and capabilities model, WooCommerce is positioning itself prospectively as an open building-block framework that should give AI assistants direct access to shop data, rather than as a ready-made AI suite.

###### Fragmented multi-shop, integration and operational structures
WooCommerce does not support multi-shop or multi-tenant functions as standard. Multiple shops are often implemented via separate WordPress installations, multisite approaches or plugins, which makes maintenance and updates considerably more time-consuming. Connection to merchandise management systems is handled through plugins or interfaces. In complex ERP scenarios, data flows are sometimes fragmented and require additional integration logic or middleware. Overall, as the number of plugins increases, so do dependencies, security risk and upgrade overhead, making clear governance rules for operations and further development essential.

###### Classification
WooCommerce is flexible, quick to get started with and particularly attractive for small to medium-sized shops — especially in content-adjacent scenarios. For larger or heavily process- and integration-driven requirements, the project and governance overhead increases considerably, as core capabilities such as tenant separation and integration management frequently have to be handled outside the standard feature set.

## 5 Positioning of JTL-Shop 6.0
Successful e-commerce platforms differentiate themselves primarily through their system architecture and operational logic, not through breadth of features.

**High process integration: platforms differ in whether they fully integrate these workflows or merely connect them via interfaces. Systems with comprehensive integration offer automated processes and consistent real-time data, while superficial solutions often require additional tools and manual effort. Especially where high requirements for stability and security apply, integration quality becomes a clear competitive advantage.**

**Localization: a platform should reflect regional and regulatory specifics directly within the system. Global standardization reaches its limits particularly in regulated markets: tax rules, data protection, legally compliant checkout, and local payment and shipping methods must be integrated. When localization is firmly embedded in the architecture, merchants are relieved of a great deal of customization effort and reliability increases.**

**Unified data foundation: platforms with a central data model manage master data, inventory, prices and orders efficiently across all channels. Solutions that offer multichannel only as an add-on feature frequently reach their limits. With a systemically integrated data model, all channels are managed in a consolidated way and operational issues are minimized — making multichannel a core function of the platform.**

**Modernity balanced with manageable complexity: in e-commerce, modular and composable architectures are increasingly gaining ground; they are flexible but often complex. Merchants are looking for a sensible compromise between modernity and ease of use. Successful platforms leverage modern principles such as API-First and Headless while taking care not to burden users with enterprise-level complexity. Practical day-to-day usability is the deciding factor.**

**AI for scalability and cost control: economic scalability is critical for commerce platforms. If fees, add-on modules or external dependencies become expensive, growth can be constrained. Platforms with automated processes and efficient architecture have the advantage. Transparent cost structures offer a competitive edge. Current market data show that AI is increasingly being used as a lever for economic scaling in retail. According to a survey by the EHI Retail Institute (2025), 55% of retail companies already use AI for forecasting and replenishment, 48% for employee support and 42% for automated copy creation. Additional application areas such as customer dialogue (34%) and image creation (30%) are also growing in importance.5 AI can reduce operational overhead while simultaneously shortening time-to-market.**

JTL-Shop targets professional mid-market merchants and growing retail organizations serving multiple channels, brands or countries. This target group requires a high-performance merchandise management and process system at medium to high complexity levels, but without the costs and structures of classic enterprise solutions. Key requirements are an economically viable, upgradeable platform

5 (EHI Retail Institute, n.d.)

as well as an open architecture for ERP integrations, multi-shop scenarios and individual commerce processes. This strategic direction forms the foundation of the product architecture.

The greatest perceived added value remains unchanged: the close integration with JTL-WaWi and the resulting process proximity. At the same time, competitive weaknesses arise less from functional gaps and more from barriers to entry, complexity, update and plugin issues, and lower usability compared to modern SaaS platforms. For JTL-Shop 6.0 this means: the strength of the WaWi must be preserved while access, operations and extensibility become significantly simpler and more cost-efficient.

The product's focus is not on fully customizable enterprise programs with maximum freedom and comprehensive governance. Such scenarios are possible, provided that customization and controllability remain within a defined platform framework. Very small merchants are not excluded, but they are not the central reference point. For them, fully standardized SaaS solutions are more economical and involve less operational overhead.

The experience from the Shop 5 ecosystem feeds into the product. That ecosystem was shaped by technically proficient merchants, agencies and service partners who value high degrees of freedom and accept complex operational structures in return. At the same time, the market comparison shows that JTL differentiates less through breadth of features and more through the process integration of the WaWi and its operational controllability. The Shop

6.0 builds on this strength and aligns it toward professional mid-market merchants who expect fast time-to-value and economical operations.

JTL-WaWi acts as the operational core for merchandise management, order processing and multichannel processes for many merchants. This deep process anchoring constitutes a difficult-to-replicate differentiator in international competition. At the same time, the product landscape has grown historically and is partly shaped by on-premise logic — modern requirements such as cloud operations, global scalability and a contemporary developer experience have so far been barely addressed. Shop 6.0 thus operates in the tension between preserving operational strengths and technical renewal.

Current architectural trends indicate a transition toward modular, API-First platforms with a clear decoupling of frontend and business logic, as well as cloud-native operational approaches. The shop thereby becomes an integral component of an extensible system landscape that can be flexibly integrated into existing and future technology stacks. Shopify and BigCommerce demonstrate the advantages of a highly standardized SaaS operating model in terms of time-to-market and operational relief. Shopware, Magento and WooCommerce, on the other hand, show that greater degrees of freedom are almost always associated with higher operational and governance overhead. For JTL, this results in an operating model that appears as straightforward and standardized as possible for merchants, without abandoning the central process proximity to the WaWi. In practice this means: SaaS-typical operational responsibility and upgrade capability on the platform side, while still providing sufficient technical depth and integration precision for more complex retail realities.

One advantage lies in JTL-WaWi as the leading system for all commercial and

operational commerce processes. While many platforms require apps, plugins

or middleware for this purpose, the WaWi at JTL forms the clear data and process core. Inventory, prices, orders and process logic remain in the ERP system, while the shop acts as the interaction, presentation and experience layer.

To support flexible retail models, multichannel and multi-shop capabilities are required: multiple storefronts, brands or countries are served from a single central data and process core. Multi-shop encompasses technical multi-shop capability, functional multi-tenant logic and controllable operational management. In the DACH region, localization, legal compliance and process proximity are also essential. The goal is a platform that structurally meets regional requirements while being based on modern, internationally compatible architecture.

External modules and an open ecosystem complement the functional scope. This is ensured by defined interfaces, clearly documented APIs and reliable middleware that enables partner solutions and extensions. Economic scalability remains particularly critical in the mid-market — through transparent cost models, controllable operating costs and an architecture that supports long-term efficiency gains.

AI features are gaining importance — both natively (e.g. copilot or experience features) and via external services. For Shop 6.0 this means that extensibility is implemented both functionally and governance-ready: via APIs, defined extension points, versioned interfaces and a controllable ecosystem. Data, processes and interaction points are made available in such a way that AI-powered workflows such as personalization, assortment logic, assistants or operational automation can be integrated.

Compared to global SaaS providers, JTL differentiates through deeper process integration and WaWi proximity. Compared to open platforms, through more consistent product logic, operations and data management. Compared to suite approaches such as PlentyONE, through a clearer separation of platform roles and greater architectural controllability in modular target architectures.

## 6 Functional and technical requirements
The operating model of JTL-Shop 6.0 is designed to support functional requirements in a stable and economically viable manner even as business volumes grow. The platform is operated as a cloud-based system capable of dynamically absorbing peak loads and rolling out feature updates in a controlled manner without disrupting ongoing retail processes.

### 6.1 API-First, interfaces, role model WaWi and shop / multichannel
The separation of responsibilities between the shop and merchandise management is often unclear for merchants in JTL-Shop 5.0. Although JTL-WaWi is the central system for product, price and inventory management, there is uncertainty about where customizations should be made. This places a particular burden on less technically experienced users and makes them dependent on service partners. For Shop 6.0, a comprehensible role model is therefore required from a technical, product-related and user perspective. JTL-WaWi acts as the operational sales core. All sales channels are connected such that orders and relevant process states are managed consistently. Multichannel emerges as a property of the platform. The goal is a seamless, cross-channel view of products, prices, inventory, orders and customers, without redundant data storage or parallel process models.

Missing APIs in JTL WaWi mean that integrations in Shop 5.0 arise as workarounds, which increases coupling and maintenance overhead. The API strategy for the connection between WaWi and Shop 6.0 implies an interface layer through which item master data, prices, inventory, customer data and orders flow between the shop level and WaWi. Data and functions are connected with graduated update requirements according to their functional criticality. Process states and critical data (in particular inventory, orders and payment) are managed and synchronized in such a way that inconsistent states, manual corrections and unnecessary integration overhead are avoided.

#### Product and catalog management
Item master data, categories, variants, prices and further product-related attributes are maintained in JTL-WaWi and transferred to the shop level via defined processes. Multiple shops share the same data foundation but can represent different assortment subsets, pricing logic or presentation formats.

On this basis, both classic catalog views and curated product collections — for example for landing pages, campaigns, or target-group-specific areas — can be designed efficiently. Business-level changes to assortment logic, prices, or attributes are maintained centrally.

#### Inventory and Availability
Inventory and availability are managed across all channels from JTL-WaWi. Reservations, stock movements, and goods receipts are processed and projected to the shop level with a currency sufficient for sellability. Configurable rules allow availability displays to be controlled depending on warehouse locations and delivery addresses, buffers, or sales priorities, without dissolving the central inventory logic.

#### Order and Order Processing
The shop handles order capture and consistently maps all steps relevant to customers — from the shopping cart through checkout to order confirmation. After the order process is completed, the required data is transferred in a structured manner to JTL-WaWi, where the actual order processing takes place. The transfer is designed so that no orders are "lost" and deviations (e.g. failed transfers) are clearly identifiable and actionable from a business perspective.

Status changes along the order lifecycle — such as payment receipt, picking, shipping, or return — are managed in the ERP system and made transparent to the customer via the shop. In this way, control of operational processes remains consolidated in the central core system, while the shop takes on the role of a customer-facing interaction and information layer.

#### Payment Processing
The shop offers merchants integrated payment methods and, via a secure and standardized payment interface, the ability to connect additional payment providers. Payment processing is carried out entirely within the shop frontend from the customer's perspective, but uses established payment service providers and methods.

The shop initiates payments, processes responses from payment providers, and transfers payment information — including the resulting payment status — in a structured manner to JTL-WaWi. The downstream processes — such as payment receipt, release for picking, or invoicing — can thus be managed unambiguously.

Different payment methods and risk profiles can be configured in a differentiated manner per shop, target group, or market segment, without fragmenting the central logic of order and financial processes in the ERP. This links the necessary flexibility in checkout with a clear, auditable mapping in commercial processes. The payment status thus remains clearly traceable as a commercial process state in the ERP and consistently controls downstream steps such as release, invoicing, and shipping, as well as further processing in financial accounting.

#### Shipping & Fulfillment
Shipping and fulfillment processes are managed in JTL-WaWi or connected logistics components. The shop provides the necessary information — such as delivery options, shipping costs, or estimated delivery times — during checkout and transfers confirmed orders with all relevant data to the ERP system.

Order-related shipping information, such as tracking IDs or status messages, flows back from the fulfillment process and can be made available to the customer via the shop. Different shipping logic per shop or market — for example, different service providers, terms, or warehouse locations — can thus be mapped without losing the overarching process context in the backend. The shop remains the interaction and information layer, while fulfillment decisions and status management are anchored in the central backend.

#### Customer & Account Management
Customers can register in the various merchant shops and manage their orders and account data. The shop ensures that the information required for processing and service reaches JTL-WaWi in a structured manner and is integrated there into the existing customer and accounts-receivable logic.

On this basis, cross-channel customer relationships can be maintained and used for service and CRM purposes in compliance with data protection requirements. At the same time, it remains transparent which interactions took place in which shop context, enabling both channel-specific and cross-channel analyses and forecasts. With their customer account, customers have the ability to view past and current orders. Features such as "reorder" increase the likelihood of repeat purchases. The view of order history, reorder options, the ability to save order lists, and a PDF invoice overview within the customer account turn the customer account into an attractive customer dashboard.

### 6.2 Regional and Regulatory Requirements
Regional and regulatory requirements are reflected in the system logic and implemented as verifiable minimum requirements for legally compliant operation in Germany and the European Union. The system addresses regional requirements through integrated features such as checks against sanctions lists, procedures for detecting potential fraud attempts, and the ability to maintain customer block lists. Analytics, tracking, and consent mechanisms in accordance with the General Data Protection Regulation are also available without any setup effort.

The shop provides operators with all necessary settings and configuration options to reliably implement legal requirements. Preconfigured systems enable an immediate sales launch for the German market with minimal initial setup effort. These concern in particular tax logic as well as the provision and maintenance of central legal texts such as privacy policies, legal notices, and other legally required information.

Regional compliance requirements are also taken into account by the system in the frontend and in the presentation of content. These include legally compliant price display including unit prices, transparent information on estimated delivery times, clearly defined cancellation processes, and the integration of all legally required mandatory disclosures in the shop. In addition, the platform supports legally compliant checkout processes and the integration of established payment and shipping methods.

### 6.3 Ease of Use and Administrative Convenience
The Shop 5.0 customer perspective shows that the greatest barriers to entry lie in the high initial setup effort, the strong dependency on technical understanding, and complex administration processes. Merchants want a significantly simpler, guided, and faster onboarding experience for shop operations. Shop 6.0 addresses these requirements through a clearly simplified and more guided user experience. An AI assistant handles setup steps, assists with configuration, and automates recurring or specialized tasks. In addition, all administrative functions are consolidated in a central, intuitive interface, complemented by clear workflows, editors, and guidance elements.

This combination of guided setup, AI-assisted automation, and consolidated administration tools significantly reduces technical barriers and enables market entry with minimal initial effort. At the same time, the

process depth of JTL-WaWi is preserved, as all design and configuration steps are consistently embedded in the central operational data logic.

### 6.4 Multi-tenancy, Multi-shop Structure, Code Reuse
The multi-shop challenge is addressed through targeted reuse of shared components. The majority of shop functionality — approximately 60 to 80 percent — is consolidated in a central core and made available to all shop instances. The shops thereby benefit from a unified codebase, which significantly simplifies development and maintenance. Shop-specific customizations are implemented via a file inheritance principle: while the standard functionality resides in the core, shops can override individual components and make individual extensions without duplicating the core code. This flexible structure ensures that only the divergent 20 to 40 percent of functionality per shop needs to be individually maintained, while the shared base remains intact for all shops. The result is a modular and maintainable solution that guarantees both scalability and customizability.

Shop operators can manage storefronts efficiently without having to use separate, isolated systems. The system distinguishes between shopfront or storefront — for example for a brand, a country, or a target group — and tenant, i.e. a legally or organizationally separate entity. Defined isolation and authorization rules apply to both levels. In this way, the platform enables reuse without multi-shop scaling leading to unmanageable complexity. All shops are controlled via a single instance of JTL-WaWi. Going forward, additional sales channels (e.g. marketplaces) can be incorporated into the same central management model.

One example is a merchant who uses the multi-shop functionality to operate a German-language shop and an English-language shop with prices in US dollars, both managed through the same inventory management system.

Another example is a merchant who operates a shop for private end customers with gross prices and individual items, as well as a shop for business customers with net prices, packaging units, and minimum order quantities. Since JTL-WaWi already provides marketplace integrations (e.g. via JTL-eazyAuction), the management model can also connect additional channels such as marketplaces or touchpoints.

### 6.5 User Experience and Visual Design, Headless PWA Frontend
All communication between frontends and backend takes place exclusively via interfaces (APIs). This ensures that the frontends operate completely decoupled from the backend logic and obtain all required data and functions via standardized web service calls. At the center is an integration or middleware layer that acts as an intermediary between JTL-WaWi and the individual shop instances. This middleware provides the necessary API endpoints for the frontends on one hand, and handles communication with JTL-WaWi — for example via the JTL connector or the JTL-WaWi REST API — on the other. This architecture allows additional services such as content management systems (CMS), search services, or other backend components to be connected in a modular and flexible manner, without requiring modifications to the existing frontends. The system thereby remains extensible, maintainable, and future-proof, as new functionality can easily be integrated into the existing structure via additional interfaces.

The headless architecture ensures that the frontend of the shops is completely decoupled from the backend. As a result, the shop instances can be implemented as independent Progressive Web Apps (PWA) that obtain their data exclusively via defined APIs. This technical decoupling enables a "lightning-fast" user experience, as the frontends operate independently of backend processes and thus achieve optimal performance.

PWAs offer numerous advantages: they support offline use by storing content locally and making it available even without internet access. In addition, they enable an app-like user experience (UX), for example through push notifications or the ability to add the app to the home screen of the end device.

To meet the demands of search engine optimization (SEO) and fast load times, Server-Side Rendering (SSR) is used. Pages are pre-rendered on the server and delivered as HTML, which improves both indexing by search engines and the time-tofirst-byte for users. Client-Side Rendering (CSR) is additionally used where interactivity is required — for example when loading data without a full page reload. Overall, this architecture provides the foundation for high-performance, flexible, and search-engine-friendly shops that can be extended at any time with new frontends or features, thanks to the API-first approach and modular structure.

By using a headless approach, the shop is flexible at the presentation layer while remaining stable in its process and data logic. The frontend is designed throughout on an interface basis.

Shop operators can offer their customers an individualized shopping experience, optimal product presentation, a conversion-oriented display (making looks to buys), and channel-specific interactions. The shop fulfills fundamental functions such as branding, trust-building, consultation, inspiration, and differentiation.

User experience means performance, a focus on mobile devices, and ensuring optimal product access. To guarantee this, options for product discovery and product placement are prioritized from the outset.

A set of predefined and reusable frontend components ensures that the visual design can be customized per shop without destabilizing central processes. Essential shop functions such as product catalog, product details, shopping cart, checkout, and customer account are developed and optimized as reusable components.

The shop interfaces are implemented as web applications. This ensures short load times, a seamless user experience, and straightforward brand-specific implementation of the interfaces. As a result, the shops gain the ability to be installed on end devices, to offer optimized mobile user interfaces, and to cache content for situations with limited connectivity. Through the headless approach, the design of the frontend is not bound to templates but can be implemented freely and in a brand-specific manner. The shop interface offers extensive design freedom and the ability to respond quickly to changing requirements.

This enables preloading of content, asynchronous data fetches, and server-side rendering to improve discoverability in search engines. Core functionality remains consistent across different devices.

### 6.6 Updates, Extensibility, and Ecosystem
Recurring problems with updates, extensions, and individual customization in Shop 5.0 show that openness alone is not an advantage if integration points, responsibilities, and upgrade paths are not clearly defined. Experience from the existing JTL Shop ecosystem shows that openness and customizability deliver significant added value for service partners and individual customer projects.

Shop 6.0 must therefore enable extensibility while simultaneously constraining it in a way that does not impair maintainability, quality assurance, or the further development of the platform. Extensions operate via defined integration points and must not uncontrollably override the core logic of the platform — such as checkout, inventory, and status logic. Interfaces and extension points are designed to remain stable, versionable, and governance-capable. This makes extensibility scalable without giving rise to role ambiguity, integration debt, or operational risks.

Stable integration points, a data foundation, and defined responsibilities form the basis for integrating additional services, frontend plugins, apps, and external tools at the business level. Additional functions such as subscriptions, product recommendations, SEO tools, or loyalty programs can be added just as easily as marketing automation, content management, or PIM solutions. Established tools — such as Klaviyo for marketing automation or social shopping integrations — are connected via interfaces and plugins in a way that preserves stability, update capability, and data consistency. Functions are extended via documented interfaces, clearly bounded configuration levels, and a controllable ecosystem. Likewise, ecosystem capability for integrating external service providers and third-party software is provided, so that partner solutions can be used productively without destabilising the platform logic.

Apps will be integrated via defined extension points and stable APIs. This enables a wide range of functions (marketing, payments, fulfilment, analytics, content, search) while maintaining controllable platform stability. Key principles include a permission based access model (e.g. via clearly declared scopes/capabilities per app), an event-driven integration model (webhooks/events instead of polling), and upgrade-safe extension points that do not require direct modifications to the theme or checkout core.

Third-party apps will be installed, configured, activated, and deactivated as needed via the control plane as distributed, versioned extension artefacts. Guardrails for performance, security, data access, and update compatibility are taken into account. The parallel initiative within the JTL cloud platform is used for the commercial provisioning and operational lifecycle of the apps. In a separate project, an app shop and a partner portal are already being built that provide core functionality for listing, purchasing, subscription/licensing, provisioning, billing, and support processes for applications. This new development is used as a central platform building block and will prospectively also be reused for the third-party apps described here in the multi-shop context. This decouples commercial processing from technical installation/activation

: the app shop/partner portal handles discovery and transaction, while the multi-shop integrates the apps into the shop runtime via defined integration points and a controlled control plane.

Prospectively, the platform also creates the foundation for agent-based commerce scenarios by making structured shop and product data available in machine-readable form, so that AI-mediated access modes can be supported in addition to classic frontend interactions.

### 6.7 AI Capabilities & Agentic Commerce Perspectives
The goal of AI integration is to automate recurring tasks, support specialist decisions on a data-driven basis, and consistently improve the quality of content and user experiences.

This includes in particular AI-assisted functions for creating and optimising product descriptions and marketing texts, processing product images, and controlling product recommendations and assortment logic. In addition, dialogue-based assistants can be deployed in the shop and administration context to support customers and shop operators with research, configuration, and support needs.

AI is understood as a functional platform capability that must evolve over time and therefore represents an underlying structural connectivity. The shop layer delivers signals and forms a machine-readable data foundation (including agentic commerce interfaces) that maps both discovery (understanding of products and offers) and transaction (checkout, identity, order status, after-sales). In addition to structured product data and unambiguous semantics, current price and availability information, clear rules on variants/bundles, and a comprehensible status logic along the order lifecycle are particularly relevant.

It follows that AI should not be described via fixed features but via the ability to connect future AI-assisted functions and external assistance systems. AI capabilities are mechanisms that turn signals from shop interactions into actionable inputs and prepare decisions from them. The shop is the customer-facing interaction layer where demand, intent, and purchase barriers become visible — for example through search queries, click paths, zero-result searches, checkout abandonments, return reasons, or repurchase rates. These signals form the basis for data-driven management that in traditional systems is often only achievable with enterprise tools. AI covers in particular: recommendations for assortment display and prioritisation (merchandising), indications of gaps in the catalogue based on actual customer demand (e.g. recurring search intents with no matching results), suggestions for improving navigation and findability, and indications of process or offer barriers in the checkout. Where changes in leading systems are required (e.g. attribution, categorisation, item structure), these are output as concrete, verifiable suggestions and implemented via an approval process — not as uncontrolled overwrites of the core logic.

With agent-based commerce models, the primary interaction point shifts to an upstream assistance layer. Users formulate their request in natural language; a system researches offers, evaluates alternatives, and prepares

transactions or executes them. In this scenario the shop becomes the connected data and transaction source, while the interaction takes place outside the actual shop interface. A current development consists of industry-wide standards that enable agents to access commerce functions via defined primitives. One example is the Universal Commerce Protocol (UCP), an open standard aimed at enabling AI interactions to be translated directly into purchasing processes, including standardised steps such as checkout, identity linking, and order management.

AI operates at interfaces and does not overwrite core logic. Areas such as pricing, inventory, payment, and orders remain governed and traceable. Retailers can review, edit, and approve recommendations and content. This applies to content, merchandising, and assortment suggestions. The use of AI requires careful handling of data; data protection and consent remain mandatory. AI relief and AI capability amplifiers for retailers are operationalised across three roles: initialisation (BUILD), ongoing operation (RUN), and continuous optimisation (IMPROVE). The shop delivers behavioural and demand signals (e.g. searches, click paths, abandonments).

#### BUILD — AI-Assisted Shop Initialisation
During shop initialisation, the JTL shop customer is supported by an AI-assisted "Shop Lead". Instead of complex admin menus and assumed e-commerce terminology, a dialogue-based process guides users through the key decisions: target audience, assortment, shipping and payment framework, basic setup, fundamental legal configuration, brand presence, and the initial construction of core page and navigation structures. Based on targeted questions, an AI engineer creates a consistent shop design from these inputs, significantly reducing barriers to entry. The shop is brought closer to the expectations of modern marketplace models in terms of ease of activation, without relinquishing the central data and process logic (WaWi centrality). The resulting shop design is understood as a consistent starting point: configuration, navigation and page structure, and an initial measurement framework (e.g. which signals will later serve as the basis for optimisation) are set up in a way that RUN and IMPROVE can build upon them.

#### RUN — Assortment, Portfolio, Fulfilment Options
During ongoing operations, the AI supports the retailer with data-driven assortment and supply chain decisions. Based on the products listed in the shop, sell-through data, search/demand signals, and return analyses, it can suggest complementary items that meaningfully extend the portfolio, generate content improvements, and increase basket values. Additionally, it can identify and suggest alternative sourcing options or dropshipping options, for example where better terms, shorter delivery times, or higher availability are available. The role of this AI is collaborative: it prepares decisions in a structured way and provides actionable options that can be implemented within the central process and data logic of the platform. Suggestions are formulated as concrete, approval-ready action packages (e.g. portfolio expansion, alternative sourcing, dropshipping options) and always take into account the leading process states and restrictions in the central backend.

#### IMPROVE — Data-Driven Optimisation & Feedback Loops
For continuous improvement, a "Shop Consultant" is deployed that evaluates search queries, click paths, conversion signals, retention, and revenue and visitor metrics, and derives prioritised recommendations for action from them.

The AI acts as a marketing expert and can be used by retailers to implement targeted campaigns in the shop by audience or topic (e.g. seasonal, time of year, Black Friday). The assistant creates, for example, landing pages, marketing elements such as banners or pop-ups, and optimises product presentation based on the chosen approach.

These recommendations or implementations are not directed solely at the retailer but can also be fed back as structured input into the other roles — for portfolio and offer optimisation, or to consistently implement content/layout or navigation improvements and product presentation.

In this way, a closed improvement cycle emerges that combines operational relief with commercial optimisation, without pushing the platform into a governance intensive customisation model. The optimisations are not implemented in isolation but are fed back as structured inputs into the other roles (INIT for structure/layout/navigation, RUN for assortment/offer/availability), creating a consistent, data-driven improvement cycle.

## 7 Architecture Overview
### 7.1 Layer Model
At its core, the architecture follows the principle of a decoupled, multi-layer application in the sense of a headless commerce approach, whose layers and their interaction are described in this chapter.

#### Frontend Layer (Storefront)
The shop instances each serve as customer-facing frontends and are implemented as independent headless web applications that retrieve their data via APIs from the backend. A shared codebase allows multiple frontends to be operated without sacrificing the benefits of separate shop instances: shared components (e.g. shopping cart logic, checkout flow) are developed once and reused across all shops, while differences (e.g. layout, branding, assortment per shop) are realised via configuration and overridable modules. The approach resembles a template system in which standard functions reside in the core and shop-specific customisations are added via a file-based inheritance/override principle — a shop can override any core component as needed, otherwise inheriting the default. This ensures that with n shops, not n times 80% of the same code has to be maintained, but only the differentiating 20% is managed individually.

The shop frontends themselves are implemented as Progressive Web Apps (PWA): they run in the customer's browser but can pre-load content, cache it offline, and offer an app-like experience (e.g. push notifications, "add to home screen"). To ensure both performance and SEO, server-side rendering (SSR) is used: this means pages are pre-rendered on the server (within the frontend layer) and delivered as HTML, so that search engines can index them optimally and users experience a fast time-tofirst-byte. CSR (client-side rendering) is used where interactivity is required (loading data without a page change). This architecture ensures highly performant and simultaneously search-engine-friendly shops. Importantly, the frontends are loosely coupled with the backend — they only know defined interfaces, but none of the details of the WaWi logic. This makes it possible to connect new frontends (e.g. mobile apps or additional shops) as needed without having to modify the backend.

#### Backend Layer (ERP and Business Logic)
In the background, JTL-WaWi serves as the central ERP system, managing all business objects — products, warehouse, orders, customers, invoices, etc. The WaWi can be seen as a data hub that reflects the current state of the business. In addition to the WaWi, there is an application component that acts as an integration and logic layer. This layer typically comprises a middleware server that mediates between the headless frontends and JTL-WaWi. This server middleware has several tasks: it provides API endpoints called by the frontends (e.g. "retrieve list of products", "create order"); it in turn communicates with JTL-WaWi via the JTL-WaWi REST API — to read or write data; and it can orchestrate multiple backend services if systems other than the WaWi are connected (e.g. a separate CMS for content pages, a search server for product search, payment gateways). In the case of Shop 6.0, the primary backend service is JTL-WaWi. The middleware handles the transformation and enrichment of WaWi data and provides the frontend with a consistent, abs-

tracted data structure for products, categories, shopping carts, and other domain objects. The JTL data (e.g. item name, prices, availability, descriptions) is mapped to this standard format so that frontends can expect the same structure regardless of the specific backend. Should an additional data provider be added later (e.g. an external PIM for product texts), the middleware can enrich this data without requiring changes on the frontend side. In addition to data mediation, the middleware also handles security (e.g. storing API keys, authenticating API calls), performance optimisation (caching frequently queried data to relieve the WaWi, bundling multiple API calls into one request), and error handling (e.g. retry logic if the WaWi is temporarily unresponsive). The middleware can be seen as a kind of adapter: it turns the ERP into a web-capable backend that can be consumed by modern frontends. Importantly, JTL-WaWi itself remains the authoritative instance for all transactional processes.

#### Communication & Interfaces (APIs and Cloud)
The frontends and the backend communicate exclusively via clearly defined interfaces (APIs). In concrete terms, this means: each shop frontend uses web service calls (REST API or, where applicable, GraphQL) to the middleware to obtain the required data or trigger actions. This architecture follows the API-first principle: all functions are provided via APIs, which not only ensures decoupling but also facilitates future extensions (e.g. the same APIs could be used by a mobile app or a partner portal). As an example: the frontend requests "product details for item X" — the request reaches the middleware, which fetches the corresponding data via the JTL-WaWi API and returns a unified JSON to the frontend containing all information (name, image URLs, price, stock level…). Conversely, the frontend signals "create new order" — the middleware receives the order data, creates an order via the WaWi API, and returns an order confirmation as appropriate. Through these clear contracts between frontend and backend, each subsystem can be modified or replaced internally as long as it continues to adhere to the interface. Since no standard integration is currently available for JTL-WaWi, the connection is established either via an existing connector or directly via the JTL-WaWi REST API to ensure a lean and efficient integration. The middleware will therefore contain its own JTL integration that encapsulates and translates JTL API calls. Since JTL-WaWi runs on-premise at the retailer's site, care must be taken to ensure that the API is accessible over the network (if necessary via VPN or cloud bridge).

#### Data Flow & Synchronisation (Data Consistency and Data Ownership)
In operation, JTL-WaWi serves as the single point of truth. When changes occur in WaWi (e.g. a new item or an updated stock level), this information is communicated to the connected shops — ideally event-driven in real time, alternatively retrieved at short intervals. The integration can be designed, for example, so that after each save operation in JTL WaWi (e.g. an item update), an API call is made to the middleware, which then propagates the changes to the affected frontends (e.g. via a cache invalidation mechanism or notifications). Conversely, incoming data (new orders, new customer registrations) is written to WaWi immediately. Synchronisation should occur as close to real time as possible in order to fully exploit the benefits (no overselling, up-to-date order status). In practice, the JTL connector already provides ongoing synchronisation of key entities such as items, stock levels, and orders — this can serve as a fallback

or parallel path; with the newly developed frontend, a direct, lean coupling via the API is the target. It is important that transactional integrity is ensured — for example, if an order has been placed in the shop, it must be guaranteed that it also arrives in the ERP (via confirmation callbacks and logging). The architecture rests on the principle of decoupling: changes to one frontend do not affect the other shops or the backend, as long as the API contracts remain stable. Likewise, JTL-WaWi can be updated or, in future, replaced by a different ERP without requiring the frontends to be redeveloped — only the middleware integration would need to be adapted.

### 7.2 Software Lifecycle Management
Staging provides a structured division of software delivery into clearly defined environment levels (stages). Each stage represents a distinct maturity level of the software and serves a specific purpose within the development, testing, and operations process.

#### _Development_

Target audience: Developers Serves the continuous development and integration of new functionality. Changes are built and tested automatically to obtain rapid feedback on stability and quality.

#### _Test_

Target audience: Testers, PM/PO

Represents a production-like environment for validating the application. Released artefacts from the Development stage are deployed here and verified under realistic conditions (e.g. integration, functional workflows, stability). In the case of a platform driven SaaS solution, this approach is essential, as no individual or customer-specific solutions are possible, since all instances share the same codebase.

#### _Production_

Target audience: Merchants, service partners

Represents the productive environment. Deployments are carried out exclusively on the basis of verified and approved artefacts. Additional release and governance mechanisms ensure that only quality-assured versions are rolled out to production.

#### Branching, Code Review and Versioning in the Development Process
The development process uses multiple branches to represent parallel development streams in a structured way. Once a feature is completed according to the Definition of Done, a pull request is raised to merge the code into the "main" branch. Part of the pull request are the PR checks, which must pass successfully, as well as a code review by a senior or lead developer.

Functional enhancements, modifications, or bug fixes can be implemented in isolation in separate feature branches and, after successful review, integrated in a controlled manner into higher-level branches.

Git is used as the version control system and code is stored in one or more remote repositories on GitHub. The specific versioning scheme — e.g. semantic versioning — will be finalised later in the project

and adapted to the requirements of the product and release cycle. This approach supports a separation of development, testing, and production delivery and integrates seamlessly into the stage-based CI/CD and staging concept.

#### Continuous Integration / Continuous Delivery (CI/CD)
The goal is a consistent, traceable, and quality-assured delivery of changes across the entire development and operations process. As part of Continuous Integration (CI), code and configuration changes are automatically integrated, built, and verified. Every change passes through defined quality and security checks before it can be promoted to a downstream stage. This ensures that errors are detected and resolved early. Continuous Delivery (CD) governs the controlled handover of verified software artefacts between the individual stages. The CI/CD pipelines are defined via GitHub Actions and executed based on defined triggers.

#### Quality Assurance
The multi-layered approach combines automated and manual testing methods to ensure high product quality and software reliability. At the heart of the concept are mature, automated testing approaches covering various technologies and frameworks:

- Unit tests with Vitest for frontend and Node.js backend modules

- Integration tests for BFF services and ERP integration workflows

- UI and end-to-end tests with Playwright

- Systematic acceptance tests for business-critical scenarios

This technical foundation ensures that both individual components and the overall system are tested comprehensively and meet the quality requirements. The three-tier environment structure enables a controlled and secure development and deployment pipeline. Each environment fulfils specific tasks within the development and testing process.

The use of GitHub Security enables comprehensive dependency and code quality management for the continuous monitoring and improvement of code quality.

## 8 Technical Architecture
This section defines the fundamental architectural principles that govern all design decisions within the JTL Shop platform and set the boundaries within which implementation decisions are made.

### 8.1 Azure-First Cloud-Native Strategy
The platform is built as a cloud-native system on Microsoft Azure.

We employ:

- Managed Infrastructure Services where appropriate

- Containerised workloads orchestrated via Kubernetes

- Infrastructure-as-Code for reproducibility and traceability

- Horizontal scalability as the default scaling mechanism

We explicitly avoid:

- On-premise dependencies

- Manual infrastructure provisioning

- Stateful runtime services

The architecture is designed to operate as a SaaS platform from day one, even where the scope of initial deployments is limited.

### 8.2 Cache-First Performance Philosophy
Performance is achieved primarily through aggressive caching, not through pure compute scaling.

We rely on:

- CDN-level caching as the primary delivery mechanism

- Redis as the first backend read layer

- Disk caching for large content types

- PostgreSQL only as a controlled fallback, not as the primary source under high load.

Backend compute is treated as a costly resource that must be protected. All read-intensive operations are designed to be cacheable, unless explicitly constrained by business rules such as the checkout process or the resolution of authenticated contexts.

When caching discipline lapses, infrastructure costs increase linearly. Cache design is therefore treated as a central architectural responsibility, not as an optimisation layer.

### 8.3 Logical Shop Isolation and Escalation Path
The platform enforces logical shop isolation at the application, query, and cache level.

We require:

- Shop and country identifiers in all access paths

- Cache keys scoped to the shop and country context

- Enforcement of token-based access at the API level

- Explicit context resolution before any execution of business logic

In the MVP, no physical database isolation per shop is implemented. However, the architecture supports escalation to shard-level or dedicated infrastructure isolation for high-volume or regulated tenants without requiring the core system to be redesigned. Isolation maturity increases over time without requiring architectural redesign.

### 8.4 Deterministic Rendering and SEO Governance
Rendering behaviour is deterministic and controlled.

We ensure:

- A clear separation between cacheable and non-cacheable pages

- Stable URL identity

- Explicit page classification

- Predictable metadata generation

SEO is not treated as a plugin feature. It is an architectural concern embedded in the routing, rendering, and caching strategy. Dynamic personalisation is restricted where it conflicts with cache efficiency or SEO clarity.

### 8.5 Upgrade-Safe Contracts and Versioning
The platform enforces strict versioning boundaries for:

- Themes

- Extensions

- APIs

- Event contracts

Backwards compatibility is governed through explicit versioning, not through implicit behaviour.

We avoid:

- Undocumented, breaking changes

- Implicit runtime coupling between components

- Cross-component side effects

This ensures that:

- Theme upgrades do not affect the shop runtime

- Extension upgrades are reversible

- Core platform upgrades do not destabilise tenant customisations

Platform governance takes precedence over unrestricted flexibility. The only exception to the above is security patches that introduce breaking changes; in such a case, prior communication with tenants would be required to enforce an upgrade.

### 8.6 ERP-Agnostic Connector Architecture
The platform is designed to integrate with external ERP systems via a generic, interface-driven connector architecture. Although the initial implementation targets the JTL-WaWi Cloud ERP, the system must not be tightly coupled to any specific ERP solution.

ERP communication is abstracted through a defined contract layer. The shop core depends only on behaviour contracts, not on concrete ERP implementations. This ensures long-term flexibility, extensibility, and architectural stability.

### 8.7 High-Level Platform Architecture and End-to-End Flow
This section describes the structural organisation of the platform and the end-to-end request lifecycle from the edge to the data layer. It defines the separation of responsibilities between the shop runtime, control plane operations, and ERP integration.

**Figure 1: High-Level Platform Architecture**

The platform is organised into clearly separated layers:

|**Layer**|**Components**|
|---|---|
|**Edge Layer**|•<br>Azure CDN<br>•<br>Web Application Firewall<br>•<br>TLS termination|
||•<br>Domain resolution|
|**Application**|•<br>Containerised shop services running on Azure Kubernetes<br>Service|
|**Runtime Layer**|•<br>Backend-for-Frontend APIs<br>•<br>Rendering engine|

||•<br>Context resolution layer|
|---|---|
|**Cache Layer**|•<br>CDN edge caching<br>•<br>Redis distributed cache<br>•<br>Disk caching for large content types|
||•<br>PostgreSQL as the primary store for structured data|
|**Data Layer**|•<br>Object storage for media and artefacts<br>•<br>Search & analytics for filtering and matching|
||•<br>Asynchronous data ingestion from JTL-WaWi|
|**Event Layer**|•<br>Event-driven update propagation<br>•<br>Backgroundprocessingservices|

**Table 12: Platform Layers**
Each layer has a single responsibility and is horizontally scalable. Cross-layer coupling is explicitly avoided.

#### End-to-End Request Flow
A shop request follows a deterministic sequence:

1. The request arrives at the CDN edge

2. Domain and tenant context are resolved

3. A cache lookup is performed

4. On cache hit → the response is returned immediately

5. On cache miss:

   - a. The request is forwarded to the Kubernetes ingress/gateway.

   - b. Context resolution is performed (e.g. shop, locale, currency).

   - c. The request is handled by stateless shop runtime services running on AKS. These services operate in a multi-tenant model, where a shared pool of runtime pods can serve multiple shops simultaneously. The platform does not assign dedicated pods to any individual shop.

   - d. The rendering engine determines the required data.

   - e. Where ERP-backed data is required, the rendering engine calls the ERP connector layer via defined interfaces.

   - f. The connector layer communicates with the ERP system via a concrete adapter implementation.

   - g. The response is mapped to the internal domain model.

   - h. The rendering engine generates the response using the template/render engine.

   - i. The Redis render cache is updated.

   - j. The CDN response is cached where possible.

Checkout and authenticated flows bypass CDN HTML caching but still make use of Redis where possible. The database is never treated as the first read layer. Instead, the platform relies on multi-layer caching (edge cache, render cache, and data caches) to ensure predictable performance and scalability.

In addition to the synchronous request path, the ERP connector layer also subscribes to ERP-based events and forwards these to the internal event system. This enables cache invalidation, projection updates, and data synchronisation without coupling internal services to ERP-specific mechanisms.

The runtime services on AKS are shared, stateless services capable of serving multiple shops simultaneously, thereby ensuring efficient resource utilisation and horizontal scalability.

**Figure 2: Overview of an Infrastructure Request**

#### Separation of Control Plane and Data Plane
The architecture separates operational control from data processing.

||**Data Plane**|**Control Plane**|
|---|---|---|
|•|Processing of all shop traffic|•<br>Tenant configuration|
|•|Stateless rendering services|•<br>Theme management|
|•|Cache-first execution model|•<br>Extension lifecycle.|
|•|Runtime routing using the resolved|•<br>Shard mapping configuration|
||shop context|•<br>Deployment orchestration|

**Table 13: Responsibilities — Data Plane vs. Control Plane**

Control plane operations do not block shop traffic. Configuration changes are propagated asynchronously and explicitly invalidate the cache.

This separation allows traffic to be scaled independently of management operations.

#### Boundaries with JTL-WaWi
The shop is not a transactional system of record. All persistent business transactions remain the responsibility of the WaWi system. This ensures

financial consistency and prevents discrepancies between the state of the shop and the state of the WaWi system.

JTL-WaWi remains, among other things, the leading system for:

- Product data

- Pricing rules

- Tax rules

- Stock

- Order persistence

- Shipping

- Voucher management

The shop does not replicate or replace the transactional logic of the WaWi system. All read operations are decoupled from WaWi via asynchronous data synchronisation.

Product search in the shop remains functional even when WaWi is unreachable. This means that all data held in the cache can continue to be displayed. However, information sourced directly from WaWi is not available in this scenario. For example, products, items, and prices can be displayed. Stock data, orders, shipping, or payment information, by contrast, are not retrievable in this scenario. Since the intention is not to replicate the entire WaWi database but only to retain product-related information, shop search remains limited under these conditions but acceptably usable.

Write operations are subject to a strict boundary policy:

- Order placement requires a successful WaWi confirmation

- Payment capture is controlled by a confirmed WaWi write operation

- If the WaWi is unavailable, the checkout switches to a controlled emergency mode and blocks the final submission of the order

- In the MVP version, the shop does not store permanent orders independently of the WaWi.

- The shop does not store permanent write operations in general, as this falls within the WaWi's area of responsibility.

The long-term development plan provides for integration with the cloud WaWi as the preferred transactional write target.

### 8.8 Rationale for technology stacks, services, AI-assisted development
The platform uses managed Azure services aligned with cloud-native best practices.

|**Layer**|**Azure**<br>**Service**|**Purpose**|**Rationale for selection**|
|---|---|---|---|
|**Edge & Security**|Azure Front<br>Door + WAF,<br>Azure API<br>Management|Global content<br>delivery and<br>perimeter protection,<br>centralization of the<br>API for the<br>backend area|Edge delivery with low latency,<br>HTML caching, integrated security<br>controls<br>Secured central gateway|

|**Frontend**<br>**Runtime**|Next.js<br>(React-<br>based<br>SSR)|Server-side<br>rendering of the<br>shop|Mature SSR framework with strong<br>SEO support, hybrid rendering<br>patterns, and large ecosystems|
|---|---|---|---|
|**Client-Side UI**|React (via<br>Next.js)|Interactive shop<br>components and<br>hydration|Shared React model for SSR<br>and client, predictable component<br>lifecycle|
|**Admin/Control**<br>**UI**|React|Administration<br>interfaces and<br>internal tools|Mature ecosystem, strong<br>component model for dashboard-<br>style applications|
|**Backend APIs**|Node.js (BFF<br>services)|API orchestration<br>and WaWi<br>integration layer|Strong ecosystem, compatible with<br>the<br>Next.js<br>runtime,<br>container-<br>friendly|
||Azure|Container|Horizontal scalability, workload|
|**Compute**|Kubernetes<br>Service|orchestration for the<br>shop runtime|<br>isolation, and portability|
|**Cache**|Azure<br>Managed<br>Redis|Distributed<br>application<br>cache|Sub-millisecond access, reduces<br>database load and delivers<br>results|
||Azure|Structured data|ACID guarantees, relational modeling,|
|**Data**|PostgreSQL<br>Flexible<br>Server|store for platform<br>projections|<br>and predictable scaling|
|**Search**|Azure AI<br>Search|Full-text search,<br>faceting, filtering|Managed search service, scalable<br>indexing, and native Azure integration|
|**Object Storage**|Azure Blob<br>Storage|Media, static<br>assets, theme<br>artifacts|Durable, cost-efficient storage with<br>CDN integration|
|**Event Backbone**|Azure Service<br>Bus, Azure<br>Event Hub,<br>Azure Web<br>Pub/Sub|Asynchronous data<br>synchronization,<br>real-time<br>notifications.|Reliable message exchange, dead-<br>letter<br>handling,<br>and<br>retry<br>mechanisms|
||AKS Worker<br>|Event<br>processing<br> <br>|Scalable event-driven processing|
|**Background**<br>**Processing**|Pods, Azure<br>Batch|and<br>projection<br>updates, recurring<br>processing||
|**Observability**|Azure Monitor<br>+ Application<br>Insights,<br>OpenTelemetr<br>y, Sentry|Metrics, logging,<br>tracing|Native<br>Azure<br>integration<br>and<br>operational<br>transparency.<br>Third-<br>party tools for additional data|
|**CI/CD & IaC**|Terraform +<br>Azure<br>Pipelines|Infrastructure<br>automation and<br>deployment|Reproducible environments, version-<br>controlled infrastructure|
|**Secrets &**<br>**Identity**|Azure Key<br>Vault|Secret management<br>and encryption|Centralized, secure key management|
||Azure OpenAI|AI-assisted|Managed access to foundation|
|**AI Support**|Service|creation of themes,<br>translations, and<br>shop content|models within the Azure ecosystem|

**Table 14: Technology stack overview**

Service selection is guided by:

- Guaranteed availability

- Alignment with the native Azure ecosystem

- Predictable cost modeling

- Horizontal scalability characteristics

- <u>Operational maturity of enterprise Azure environments</u>

All runtime components remain containerized and portable at the workload level, preventing tight coupling to proprietary runtime services.

#### AI-assisted development
AI is used as a supporting function within the software lifecycle to improve delivery speed, consistency, and efficiency. It is integrated in alignment with the platform's architectural principles: clear responsibilities, controlled lifecycle, and full traceability. AI supports the workflow but does not replace technical responsibility or decision making.

#### Principles and boundaries
The use of AI is subject to strict governance rules:

- All AI-generated outputs must be reviewed before use by the WaWi

- Architecture, security, and operational constraints always take precedence

- No automated or unreviewed changes are made to production systems

- AI must not cause implicit dependencies or unclear system behavior

AI is positioned as a productivity layer, not as an autonomous execution mechanism.

#### Use in the software lifecycle
AI is deployed selectively across the entire development lifecycle to support specific activities. A list of recommended AI tools is available in the appendix.

|**Area**|**Purpose**|**AI usage **|
|---|---|---|
|Ideation &<br>exploration|Supporting the thought<br>process and solution<br>finding in the early<br>phase|AI is used to explore solution options, challenge<br>assumptions, compare approaches, and structure<br>initial ideas prior to formal specification.|
|Documentation|Ensuring consistent<br>documentation aligned<br>with<br>the system|AI assists with summarization, updating<br>documentation, and explaining architecture and<br>system behavior to ensure<br>that the documentation reflects the current state of<br>the platform.|
|Backlog &<br>specifications|Structuring and<br>refining requirements<br>into actionable tasks.|AI helps translate requirements into structured<br>tasks, refine specifications, and ensure consistency<br>between product intent and implementation scope.|
|Implementation|Supporting<br>development within<br>defined architectures<br>and patterns.|AI assists with code generation, refactoring, and<br>pattern reuse, always<br>taking into account the existing architecture,<br>conventions,and constraints.|
|Quality & review|Improving code quality<br>and reducing risks|AI analyzes changes, highlights potential issues,<br>and helps reviewers identify risks related to<br>performance, security, and maintainability<br>to identify.|
|Testing|Increasing reliability<br>and test coverage|AI supports the creation and improvement of test<br>cases, helps identify edge cases, and strengthens<br>validation of system behavior.|

|Troubleshooting|Reducing the time to<br>resolve errors and<br>incidents.|AI assists with analyzing logs, identifying potential<br>root causes, and suggesting resolution approaches<br>during troubleshooting and incident handling.|
|---|---|---|
|Communication|Ensuring transparency<br>and traceability of<br>changes.|AI helps summarize changes, create release<br>notes, and document technical decisions to<br>improve shared understanding between<br>teams.|

**Table 15: AI usage in development**
#### Specification-driven development
Specification-driven tools (e.g., Spec-Kit) can transform structured specifications into implementation artifacts. In this project, they are used to improve clarity, consistency, and alignment between requirements and implementation.

Generated artifacts are subject to the same review, validation, and governance processes as manually written code. Specification-driven development supports implementation but does not replace architectural control or technical responsibility.

#### Context Integration (MCP)
AI capabilities can be extended through controlled integrations with platform systems (e.g., via MCP — Model Context Protocol).

This enables AI to interact with real-world system contexts, such as:

- Ticketing systems (e.g., Jira)

- Design systems (e.g., Figma)

- Repositories and pull requests (e.g., GitHub)

These integrations support workflow automation and efficiency but must follow the same security, access control, and audit principles as the rest of the platform. AI is used as a controlled supporting function within the software lifecycle. It improves efficiency while ensuring system integrity, maintainability, and clear responsibilities.

### 8.9 Rendering and SEO architecture
The shop implements a hybrid server-side rendering model designed to maximize SEO effectiveness while ensuring predictable performance and infrastructure costs. Rendering behavior is deterministic and governed by platform rules, not by the behavior of themes or extensions.

The rendering architecture is aligned with a cache-first delivery strategy. Pages are classified into cacheable and non-cacheable categories based on their SEO role, personalization sensitivity, and transactional impact.

#### Hybrid SSR strategy
The shop uses hybrid SSR as the default rendering model; static content is pre generated (e.g., landing page or "About us").

We enforce the following:

- Server-side rendering for SEO-critical pages and the first-load experience

- CDN caching of eligible HTML responses

- Revalidation and updates driven by TTL and published events

- Client-side rendering for highly personalized or session-bound components

This model ensures that SEO and performance scale independently of backend compute capacity. Region group and currency resolution occurs after the initial HTML rendering via controlled API hydration. Public HTML remains identical across region groups for the same shop and locale.

#### Page classification model
Pages are classified by their rendering and caching behavior. This classification is a platform-level contract and cannot be overridden by themes or extensions.

Page classes include:

- Entry and navigation pages, such as the homepage and category landing pages

- Listing pages, such as product listings in categories

- Product detail pages

- Content pages, such as CMS-driven editorial pages

- Search and filter result pages

- Account and authenticated pages

- Cart, checkout, and payment pages

**Summary:**

|**Page type**|**Indexed**|**CDN HTML**<br>**Cached**|**Notes**|
|---|---|---|---|
|Homepage|■<br>v|~~v~~<br>~~■~~|Publiclycacheablepage|
|Category|■<br>v|~~v~~<br>~~■~~|SEO-critical listing page|
|Product detail|■<br>v|■<br>v|SEO-critical page|
|CMS content|~~v~~<br>~~■~~|~~v~~<br>~~■~~|Public content page|
|Search results|-●|●<br>-|Runtime-rendered to avoid index<br>pollution|
|Account|~~-●~~|●<br>-|Authenticated|
|Cart|●<br>-|●<br>-|Session-bound|
|Checkout|●<br>-|~~-●~~|Transaction-bound|

**Table 16: Page type comparison**

Search and filtered result pages are generally not indexed and not stored in the CDN HTML cache. However, search pages for categories may be indexed. They continue to be rendered at runtime to maintain SEO transparency and avoid index pollution.

#### SEO identity and metadata governance
SEO identity is derived exclusively from the shop and language context.

Region group, currency, and B2B context have no influence on canonical URLs or indexable HTML. Price differences and market segmentation do not create independent SEO identities.

We enforce the following:

- Stable canonical URLs

- Controlled indexing rules per page class

- hreflang generation aligned with the country strategy

- Centrally managed robots directives

-

|**Context element**|**Influences SEO identity**|**Influences pricing /**<br>**runtime behavior**|
|---|---|---|
|**Shop**|■<br>v|■<br>v|
|**Locale**|~~v~~<br>~~■~~|■<br>v|
|**Region group**|●<br>-|■<br>v|
|**Table 17: SEO identity overview**<br>**Currency**|●<br>-|~~v~~<br>~~■~~|
|**B2B context**|●<br>-|■<br>v|

Themes and extensions may contribute to content, but they cannot alter the SEO identity rules or indexing policies.

#### Personalization boundaries
Personalization is constrained to ensure cache efficiency and SEO determinism.

We enforce the following:

- No CDN caching of user-specific HTML

- Session- and identity-based rendering only for authenticated routes

- Personalized fragments are loaded on demand via client-side calls

- Clear separation between publicly cacheable content and private dynamic content

This boundary is critical for future features such as B2B price transparency and tenant-specific permissions, without compromising cache effectiveness.

#### Edge HTML caching strategy
CDN caching is a preferred architectural component.

We enforce the following:

- Cache keys restricted exclusively to store and locale

- Currency and region group are excluded from the HTML cache scope

- Controlled use of Vary headers is limited to what is technically necessary

- TTL-based caching for public pages

- Explicit cache busting on publication events for high-value pages

- Stale-when-revalidate behavior where supported

Price and region-specific adjustments are resolved after initial rendering via API calls. This keeps public HTML deterministic, cacheable, and SEO-safe. Checkout and payment pages are explicitly excluded from CDN HTML caching. **Rendering lifecycle: draft vs. published**

Rendering is governed by the content lifecycle status.

We enforce a lifecycle that separates:

- Draft content for preview and staging

- Published content eligible for CDN caching and indexing

- Versioned releases for themes and templates

Publication events trigger:

- Cache invalidation for affected routes

- Sitemap update

- Search indexing signals where applicable

### 8.10 Themes and template architecture
This section describes how the shop presentation is structured, versioned, and managed. Themes are treated as controlled artifacts within a managed runtime environment, not as environments for unrestricted code execution. The architecture emphasizes upgrade safety, deterministic rendering, and controlled extensibility.

#### Immutable theme artifacts
Themes are packaged as immutable artifacts.

We enforce the following:

- Versioned theme bundles

- No in-place modification of active theme versions

- Deployment via controlled publication operations

- Rollback capability to previous maintained versions

Theme artifacts are stored in object storage and deployed via the control plane. Runtime services load themes in read-only mode. This prevents runtime drift and uncontrolled state changes.

#### Presets and override layers
Theme configuration is separated from theme implementation.

We enforce the following:

- A base theme structure

- Configuration presets at shop level

- Content-driven overrides managed via structured configuration rather than code changes

Overrides are applied declaratively at render time.

This ensures that:

- A single theme version can support multiple shops

- Configuration changes do not require redeployment

- Upgrades remain predictable

- Configuration changes can be reused across multiple shops

#### Slot-Based Composition Model
The page structure is governed by a slot-based composition model.

We enforce the following:

- Defined layout slots per page type

- Controlled insertion points for components

- No arbitrary DOM insertion

- Clear boundaries between core layout and injected elements

This model enables extensibility while preserving layout integrity and performance guarantees.

#### Theme Lifecycle and Version Management
Themes follow a controlled lifecycle:

- Draft

- Validation

- Published

- Deprecated

- Removal

Triggers for publishing a theme version:

- Cache invalidation for affected routes

- Update of SEO artifacts

- Version binding to target shops

Themes cannot bypass validation checks. Backward compatibility is managed through explicit versioning of references per shop.

#### Theme Isolation and Execution Boundaries
Themes do not execute backend business logic.

We enforce:

- Presentation logic only

- No direct database access

- No arbitrary network calls

- No uncontrolled script execution

Dynamic data access is performed exclusively through the rendering runtime APIs. This

**ensures that:**

- Theme authors cannot compromise data integrity

- Runtime performance remains predictable

- Security boundaries remain intact

Extending theme capabilities remains possible with this approach.

#### AI-Assisted Theme and Content Creation
The platform supports the use of artificial intelligence as an assistive function for creating, configuring, and managing themes and content.

AI functionality runs exclusively in the control plane and is not part of the shop request path. Runtime rendering behavior remains deterministic and is not influenced by AI inference.

Potential use cases include, among others:

- AI-assisted theme creation and layout configuration

- Automated generation of product descriptions and CMS content

- Support for automated translation and localization

- Assisted configuration of shop components and layouts

We place emphasis on:

- AI-generated artifacts must go through the same validation, publication, and versioning cycle as manually created artifacts

- AI generation takes place before publication and is not executed during the processing of shop requests

- Published artifacts become immutable inputs to the rendering system

This ensures that AI assistance does not affect caching behavior, SEO determinism, or runtime performance.

AI features may leverage managed foundation models through the Azure AI ecosystem, such as the Azure OpenAI Service. These services provide access to large language models and generative capabilities without the platform having to operate its own model training infrastructure.

The platform does not rely on proprietary AI models for core runtime behavior in the MVP. AI is treated as an optional assistive function that increases productivity while preserving architectural stability.

### 8.11 Extensions Platform
This section defines the extension model that enables functional expansion without compromising the platform's stability, security, performance, or upgradeability. Extensions are treated as regulated artifacts that execute within controlled boundaries. They must not become a second application runtime environment within the shop.

Extension refers to the technical extension artifact (e.g. UI contribution, event subscription, API integration) that executes within the defined platform boundaries. App refers to the distributive and commercial wrapper (listing, licensing, billing, support) around one or more extensions. Third-party providers therefore typically deliver "Apps" that technically consist of versioned extensions and can be installed and managed via the control plane.

The platform prioritizes operational safety over unrestricted extensibility.

#### Extension Packaging and Delivery Model
Extensions are delivered as immutable, versioned artifacts.

We mandate:

- A standard extension package format with explicit metadata

- Versioned releases with semantic versioning rules

- An explicit compatibility declaration with respect to platform and theme versions

- Controlled distribution via a platform-managed extension registry

Extensions are never installed by copying files into runtime containers. Installation is a control-plane operation that requires user consent. This ensures that the introduction of extensions is auditable, repeatable, and reversible. Going forward, distribution (listing/discovery) and commercial processing (purchase, license/subscription, provisioning) will be handled through the JTL cloud platform's app store and partner portal; technical installation and activation remain decoupled from this and continue to be handled in a controlled manner via the shop's control plane.

#### Capability-Based Permission System
Extensions operate according to a capability model.

We enforce the following:

- Explicit declaration of required capabilities at installation time

- Verifiable permission grants by tenant administrators

- Default denial for all undeclared capabilities

- Fine-grained capability scopes aligned with platform boundaries

Typical capability categories include:

- UI contributions and slot placement

- Access to specific shop APIs

- Read access to selected data projections

- Webhook or event subscription

- Contributions to the admin user interface

Extensions are not granted unrestricted access to tenant data or internal services.

#### Runtime Isolation and Sandboxing
Extensions do not execute arbitrary backend code in the MVP.

We enforce the following:

- No direct database access

- No arbitrary outbound network calls from the extension runtime

- No ability to modify rendering contracts or routing logic

- No uncontrolled script injection into cacheable HTML. Extensions

interact with the platform via:

- Approved API contracts

- Approved UI contribution mechanisms

- Approved event subscriptions

This guarantees:

- Cache determinism

- Predictable performance

- Security boundaries

- Upgrade safety

A controlled sandboxing model may be introduced at a later stage but is explicitly not part of the MVP.

#### Lifecycle Management and Version Pinning
Extensions go through a controlled lifecycle.

We enforce the following:

- Install, activate, deactivate, update, and uninstall as explicit control-plane operations with user confirmation

- Version binding per shop

- Rollback capability to previously approved versions

- Safe mode that allows extensions to be deactivated without downtime

Extension upgrades are not applied automatically to all shops. Shops must actively select new versions to avoid compatibility-breaking changes. Commercial lifecycle (e.g. purchase, renewal, cancellation, license change) is handled via the app store/partner portal; operational management within the shop platform covers installation, activation/deactivation, version selection, and rollback via the control plane.

#### Governance, Rate Limits, and Kill Switches
The platform retains control over extension behavior in production.

We enforce the following:

- Runtime guardrails and rate limits for extension-driven API calls

- Observability of the performance impact of extensions, including latency and error rates

- A kill-switch mechanism to disable an extension globally or per shop

- Mandatory logging of extension lifecycle operations

Extensions that compromise stability or security can be disabled without redeploying the shop runtime. This is an essential safety mechanism of the platform.

#### Process Description for Extensions
Based on the current extension concept, the MVP approach for extensions can be described as follows: The fundamental idea is that developers submit their extensions to a central extension registry. This registry stores extension packages in an immutable, versioned manner. This creates a controlled access point where checks such as package validation, code and security checks, and compatibility checks are performed before an extension is approved for installation.

Each extension must declare the capabilities it requires in the app manifest. This includes which platform APIs it intends to access, which shop and user permissions are required, and which extension points it connects to. Before an extension can be installed in a shop, the shop operator must explicitly approve the requested permissions. This consent serves as the basis for controlled access to the APIs. The actual data flow within the extension remains largely in the developer's hands. For example, a third-party extension may call its own backend or external services. However, if it wants to access JTL platform APIs or shop data, this must be done through the permissions and capabilities approved in the manifest. It is also important to distinguish between first-party and third-party apps:

- First-party apps are developed and operated by JTL itself. Their backend runs within the platform boundaries and enables deeper integration with the platform.

- Third-party apps come from external partners. Their backend is typically located outside the platform, which is why stricter controls regarding permissions, data access, API usage, security checks, and compatibility are required for them.

The app becomes part of the storefront rendering model. The extension is installed in a specific shop/storefront context and rendered by our platform backend in the respective shop.

In the current JTL app model / app store model, the app is primarily registered and connected as a JTL platform app (independently). This means JTL platform apps can exist and run independently, while shop extensions become usable when installed in a shop and rendered via the shop page. The technical models therefore differ, so both should be regarded as distinct extension models, but ones that are complemented by the app store and the partner portal.

### 8.12 Multi-Tenant, Shop, Locale, and Currency Model
This section defines the structural context hierarchy used to resolve identity, configuration scope, pricing behavior, and access boundaries within the platform. The shop is designed as a SaaS multi-tenant system. A tenant can operate multiple shops, with each shop supporting multiple locales and region-based pricing policies. Context resolution is deterministic and is performed before rendering, caching, theme composition, or extension execution.

#### Tenant and Shop Model
A tenant represents the ownership boundary for shops and users.

We define the following:

- A tenant may own multiple shops

- A shop represents the boundary for branding, domain, and configuration

- Each shop is mapped to exactly one custom domain in the MVP.

- Users belong to a tenant and are granted role-based permissions

- Permission checks are enforced in the control plane and management APIs

Shop configuration and lifecycle are independent of structural constraints of the WaWi system.

#### Logical Isolation Strategy
Isolation in the MVP is logical rather than physical.

We enforce the following:

- Shop and locale identifiers required in all API access paths

- Token-based authentication bound to the shop context

- Strict filtering of queries by shop

- Cache keys scoped by shop and locale

- Cross-tenant reads are not permitted under any circumstances

Physical database isolation per tenant is not implemented in the MVP. Isolation maturity increases over time without requiring architectural redesign.

#### Extending Isolation to Dedicated Shards
The architecture supports stronger isolation without redesign.

We enforce the following:

- A routing abstraction that can map shops to database partitions or shards

- Shard assignments managed by the control plane

- Transparent routing that requires no changes to themes or extensions

This enables:

- Dedicated infrastructure for high-volume tenants

- Isolation for regulated tenants

- Performance containment for outlier shops

#### Context Resolution Model
Each incoming request resolves a deterministic context tuple:

- shop_id

- locale

In addition, a policy layer resolves the following:

- region_group

- Currency

We enforce the following:

- Shop resolution based on the host header

- Locale resolution based on the path prefix

- Region group resolution based on the country identifiers configured in the shop

- The German market as the fallback when the region cannot be resolved

- Currency derived from the region group configuration

Region group and currency influence pricing and availability but do not generate independent SEO identity variants.

**Figure 3: Context Resolution Model**

#### Locale Strategy
Shops can support multiple locales.

Each shop defines a default locale that is used when a request does not explicitly specify a supported locale.

We mandate:

- The locale is expressed via a path prefix

- The language is included in the HTML cache scope

- hreflang generation is strictly locale-based

- Controlled redirect rules for missing locales

SEO identity is derived exclusively from shop and locale.

#### Currency Strategy
Currency is governed by shop policies and the region group configuration.

We enforce the following:

- Currency is derived from the region group

- Currency affects price display only

- Currency does not generate separate canonical URLs

- Price calculation is performed via region-specific APIs after the initial HTML rendering

The platform does not introduce uncontrolled currency conversion logic in the MVP.

#### B2B Context Layer
B2B functionality is layered on top of the base shop context model.

The platform operates two identity layers:

- Tenant management via the admin user interface for user and shop management

- Shop-specific buyer identities for B2B and authenticated shop usage

We enforce the following:

- B2B buyer accounts are scoped to a shop, not to the tenant management layer

- B2B buyer tokens are evaluated strictly within the shop context

- Tenant administration permissions are never granted to B2B users

- Role-based purchasing permissions are enforced at checkout

- Organization-level spending limits are checked in authenticated flows

- B2B pricing and entitlements are determined via API calls after authentication

- B2B/B2C buyer accounts may switch between scopes

The B2B context must not:

- Affect public, cacheable HTML

- Affect canonical URL identity

- Create separate SEO variants

B2B behavior is confined to runtime only and is bound to authentication.

### 8.13 Domain and Routing Architecture
This section defines how traffic is mapped to the correct tenant and shop context, how locale is represented in URLs, and how custom domains are integrated and secured. Routing is deterministic and enforced at the edge of the platform.

The MVP supports one custom domain per shop. A tenant can operate multiple shops, each with its own domain.

#### Custom Domain Management
Each shop is bound to a single canonical domain.

We enforce:

- Verification of domain ownership before activation

- An explicit link between domain and shop

- Only one domain per shop in the MVP version

- No platform-managed subdomain hierarchy

Tenants manage DNS configuration externally.

The platform only handles verification and certificate provisioning.

#### SSL and Certificate Automation
TLS is mandatory for all shop traffic.

We enforce the following:

- Automated certificate provisioning

- Automatic certificate renewal

- No manual certificate upload process

The certificate lifecycle is isolated from the shop runtime services.

#### Tenant-Aware Routing Resolution
Routing resolution occurs before runtime execution.

We enforce the following:

- Host-based shop resolution

- Immediate rejection of unbound domains

- Deterministic routing, independent of the backend runtime state

Shop resolution occurs before:

- Cache lookups

- Rendering

- Theme loading

- Extension execution

This prevents cache leakage and misdirected routing between shops.

**Figure 4: Routing Resolution Overview**

#### Locale and Domain Strategies
The locale is expressed as a path prefix. We enforce the following:

- A canonical URL structure per shop and locale

- Strict localization prefixing

- Redirect rules for missing locales

- Canonical tag generation in accordance with the locale

The region group policy does not create separate indexable URL variants.

#### CDN and Host-Based Routing Integration
Azure Front Door acts as:

- Global entry point

- TLS termination layer

- Host-based router

- Edge caching layer

- Security perimeter

We enforce the following:

- HTML cache keys scoped exclusively to shop and locale

- Checkout and authenticated routes bypass HTML caching

- WAF policies are applied uniformly across all shops

The routing is designed to maximize edge caching efficiency while preventing leakage between tenants.

### 8.14 Data and Storage Architecture
This section describes how structured data, image files, and video files are stored, segmented, and evolved within the shop platform.

The data architecture is designed to support:

- Logical isolation between tenants

- High read throughput

- Event-driven synchronization

- Controlled evolution toward stronger isolation where required

The shop is not the system of record for the transactional logic of the WaWi system. It manages controlled projections optimized for read performance and rendering.

#### Structured Data Model
The platform uses PostgreSQL as the primary structured data store for shop projections.

We enforce the following:

- Relational modeling for catalog, configuration, and projection data

- Explicit foreign key relationships where appropriate

- Strong consistency guarantees for platform configuration

- Controlled denormalization to improve read performance where justified

The shop database contains:

- Product projections

- Category projections

- Shop configuration

- Theme bindings

- Extension bindings

- Region and pricing configuration

- SEO metadata projections

The database does not replace the transactional responsibility of the WaWi system, and certain areas could be migrated to the WaWi cloud. Orders, inventory data, tax logic, and accounting status remain the responsibility of the WaWi system. Shop data represents read-optimized projections of WaWi data.

#### Sharding and Partitioning Strategy
In the MVP, the platform runs on a shared PostgreSQL cluster.

We enforce the following:

- Logical isolation through shop_id scoping

- Indexed access paths including shop identifiers

- Query patterns designed to avoid full table scans across tenants

Partitioning and sharding are not mandatory in the MVP. However, the schema design provides for:

- Table partitioning by shop

- Migration to multiple database clusters

- Dedicated shards for high-volume tenants

Escalation to shard-level isolation must not require changes to themes, extensions, or rendering contracts.

#### Tenant and Shop Data Segmentation
Data segmentation is logical and enforced at multiple levels.

We enforce the following:

- tenant_id in all cross-tenant tables

- shop_id in all shop-related tables

- Mandatory context resolution before the execution of every database query

Cross-tenant joins are prohibited. Administrative queries spanning multiple tenants are restricted to control-plane contexts.

#### Shard Routing Control Plane
The platform contains an abstraction layer for shard routing, even though a single shard is used in the MVP.

We enforce:

- Shop-to-shard mapping managed in the control plane configuration

- Transparent routing based on the resolved shop context

- No hard-coded database endpoints in runtime services

This abstraction enables:

- Moving a shop to a different shard without redeploying the application

- Isolation of high-traffic shops

- The introduction of regional database strategies in the future

Shard routing logic remains deterministic and is managed centrally.

#### Media and Asset Storage Strategy
Media and assets are stored separately from structured data.

We employ:

- Azure Blob Storage for product media and static assets

- Immutable object storage for theme bundles

- CDN integration for media delivery

- Disk caching for large content types

- No direct public access to origin storage without edge control

Media storage is scoped at the shop level at the object key level. Large binary assets are never stored in PostgreSQL. Theme artifacts and extension bundles are versioned and stored as immutable objects.

#### Projection vs. Source-of-Truth Boundaries
The shop database manages projections derived from WaWi events.

We enforce the following:

- A clear distinction between projection tables and platform-owned configuration tables

- Event-driven updates from WaWi

- Idempotent projection updates

- Explicit invalidation triggers upon changes to projection data

All duplicated records must:

- Be reconstructable from WaWi exports or event replays

- Be updated exclusively via the synchronization pipeline

- Never be treated as independent sources of transactional data

We explicitly do not:

- Replicate the full WaWi transactional logic in the storefront

- Allow projections to become authoritative business records

Projection lag is tolerated within defined consistency boundaries, as defined in section 8.10. The shop does not attempt to reconcile WaWi inconsistencies.

**Figure 5: Overview**

#### Data Evolution and Migration Strategy
Schema evolution is controlled and versioned.

We enforce the following:

- Migration scripts versioned in parallel with application code

- Backward-compatible schema changes wherever possible

- Zero-downtime migration patterns for high-traffic tables

- An explicit review process for destructive schema changes

Evolution of the data model must not affect:

- Theme contracts

- Extension APIs

- Cache key composition

- Identity representation rules

#### Search and Filtering Strategy
Search and filtering require a dedicated query model optimized for faceting, relevance ranking, and high read volumes.

We enforce the following:

- Search and filter results pages are conditionally indexed

- Search results are generated dynamically at runtime

- Search correctness is eventual and aligned with the guarantees for projection updates

The search index is built from the same event-driven projection pipeline as the PostgreSQL read model.

We ensure:

- Idempotent index updates

- Indexing fields at shop and locale level

- Region group and currency are treated as pricing context, not as SEO identity

- Explicit schema management for indexed fields

- Controlled full reindexing procedures upon structural changes

Search indexing is performed at the shop level to prevent cross-tenant contamination.

Index updates are triggered by:

- Product update events

- Category update events

- Shop configuration changes that affect visibility

- Theme publications where structured content affects searchability

Search index lag is tolerated within defined consistency boundaries and has no impact on transactional correctness.

### 8.15 Caching Architecture
Caching is not an optimization layer in this platform. It is a load-bearing pillar of the architecture.

The shop is designed to operate in a cache-first model, where compute and database layers are protected by deterministic cache behavior.

Non-compliance with cache discipline directly increases infrastructure costs and reduces scalability.

The caching architecture consists of two main layers:

- Edge caching at the CDN level

- Application-level caching using Redis. Both layers are

explicitly controlled and can be managed.

#### CDN Strategy
The CDN layer is the first read boundary for public shop traffic.

We enforce the following:

- HTML caching for eligible public pages

- Host-based routing with cache scoping by shop and region

- No HTML caching for checkout, cart, or authenticated routes

- WAF and security policies applied at the edge level

- Controlled TTL policies per page class

CDN caching reduces the compute load on the backend and levels out traffic spikes. Public HTML is identical across region groups for the same shop and locale. Price and region-specific adjustments are resolved via API hydration after the initial rendering.

The CDN is not used for:

- User-specific HTML

- Checkout state

- Authenticated sessions

Edge caching must remain deterministic and independent of personalization logic.

#### Redis Strategy
We enforce the following:

- Redis as the first backend read layer before PostgreSQL

- Projection caching for catalog and configuration queries

- Strict key namespaces by shop

- Controlled memory usage with eviction policies aligned to data criticality

Redis is used for:

- Frequently accessed product projections

- Category trees

- Shop configuration snapshots

- Computed SEO metadata projections

- Price matrices for region groups

**Redis is not used as:**

- A data capture system

- A persistent event store

- A substitute for WaWi state

All Redis entries can be reconstructed from PostgreSQL projections or WaWi events.

#### Cache Key Design and Context Scoping
The cache key design reflects the context resolution model.

We enforce the following:

- HTML cache keys scoped by shop_id and locale

- No currency or region_group in HTML cache keys

- API cache keys scoped by shop_id, region_group, and, where required, currency

- An explicit separation between public and authenticated cache scopes

Example HTML key structure: "shop:{shop_id}:locale:{locale}:route:{path}" Example price API key structure:

"shop:{shop_id}:region:{region_group}:currency:{currency}:product:{id}"

The cache key design prevents:

- Data leakage between tenants.

- Cross-shop contamination

- Region-based SEO fragmentation

All cache keys are deterministic and reproducible.

#### TTL and Invalidation Philosophy
TTL values are defined by the page class and the data change dynamics.

We enforce the following:

- Short TTL for high-volatility catalog pages

- Longer TTL for pages with stable content

- Explicit invalidation triggered by publish events

- Event-driven invalidation upon changes to WaWi projections

- "Stale-while-revalidate" where supported by the CDN

Invalidation sources include:

- Product update events

- Category update events

- Theme publications

- Extension lifecycle changes

- Shop configuration updates

Cache invalidation is performed explicitly, not implicitly, for relevant sources. The system does not rely solely on TTL expiry to ensure correctness.

#### Cost Control Through Caching Discipline
Infrastructure costs are directly linked to cache efficiency.

We enforce the following:

- Continuous monitoring of the CDN hit rate

- Monitoring of the Redis hit rate

- Alerts upon declining cache effectiveness

- Safeguards preventing uncontrolled bypassing of cache layers

A decline in the CDN hit rate increases backend request volume linearly. A decline in the Redis hit rate increases database load and compute costs.

Cache metrics are treated as primary operational KPIs. Degradation of cache performance is considered an architectural regression, not an operational anomaly.

### 8.16 Event and Synchronization Model
This section describes how the shop platform ingests data from JTL-WaWi, maintains read-ready projections, and propagates changes across the storage, cache, and search layers.

The synchronization model is designed to minimize dependency on WaWi runtime availability. Browsing remains functional even during WaWi performance degradation. Transactional write operations remain confined to the WaWi domain and are not compensated by the shop platform.

#### JTL-WaWi as Source of Truth
JTL-WaWi remains the authoritative source of truth for:

- Catalog master data

- Pricing rules and tax logic

- Inventory data

- Order continuity

- Shipping status

- Voucher management

The shop platform does not attempt to replace the WaWi logic. We

enforce the following:

- Shop data is treated as projections derived from the WaWi state

- The correctness of projections is bounded by synchronization guarantees

- WaWi availability is not required for read traffic once projections are in place • Checkout operations and order submission require WaWi system availability and confirmation

#### Initial Import and Incremental Synchronization
The platform supports two synchronization phases:

1. Initial import.

2. Incremental synchronization.

The following applies to the initial import:

- Controlled bootstrap process per shop

- Full catalog import into PostgreSQL projections

- Initial indexing in Azure AI Search

- Cache warm-up strategy for core routes where possible

We enforce the following for incremental synchronization:

- Change propagation via events rather than polling

- Idempotent updates of projections and search index

- Explicit handling of deletions, reversals, and visibility changes

The initial import establishes the correct baseline. Incremental synchronization keeps the projections up to date.

#### Event-Driven Propagation Model
The platform uses asynchronous event propagation as the standard integration mechanism.

We guarantee:

- Events are transmitted from our side via Azure Service Bus/Azure Event Hub and from WaWi/WaWi via the event system

- A defined event contract for each entity type, including versioning

- Consumers update PostgreSQL projections and Redis caches

- Search index updates are triggered as part of the projection pipeline

Propagation targets include:

- PostgreSQL projection tables

- Redis cache entries

- Azure AI Search index documents

- CDN invalidation triggers, where applicable

Event processing is isolated from shop request handling. The event backlog does not directly impact read performance, but does increase latency.

**Figure 6: Event Processing Overview**

#### Consistency Guarantees and Constraints
The synchronization model provides consistency for read projections.

We guarantee:

- No real-time synchronization guarantees in the MVP

- Defined latency tolerance for catalog and price projections

- Deterministic cache invalidation based on projection updates, not on WaWi availability

Constraints are explicit:

- Search results may lag behind WaWi changes

- Prices displayed via API hydration may reflect the most recently processed projection state, not necessarily the absolute current WaWi state

- Stock levels displayed in browsing flows are indicative only and may be delayed

Transactional correctness is maintained because:

- Checkout and order submission require WaWi confirmation

-

|**Error Scenario**|**Impact**|
|---|---|
|WaWi unavailable|Browsing continues based on projections; checkout is blocked|
|Event delay|Data freshness degrades; browsing continues|
|**Table 18: Error Scenarios**<br>Consumer error|Affected projections remain stale until a retry or replay occurs|
|Search index error|Search results maylagbehind the projection state|

The platform prioritizes read availability over real-time freshness.

#### Error Handling and Replay Strategy
The eventing system is designed for reliability under failure conditions.

We enforce the following:

- Retry semantics for transient failures

- Dead-letter queue message handling

- Manual and automated retry mechanisms for recoverable errors

- Idempotent consumers enabling safe reprocessing

Failure modes include:

- WaWi event transmission failure

- Message delivery delays

- Consumer processing errors

- Projection write conflicts

- Indexing errors

**Measures include:**

- Monitoring of event backlog and consumer lag as primary KPIs

- Alerting on sustained lag exceeding defined thresholds

- Controlled replay to restore projection correctness after incidents

Event replay restores projections without requiring direct access to WaWi at runtime, provided that base data can be restored via re-export or a snapshot if needed.

### 8.17 Security and Isolation Model
This section defines the multi-layered security controls that protect tenant data, platform integrity, and operational stability.

Isolation in the MVP is logical rather than physical, and is enforced systematically at the identity, data access, runtime, and network layers.

Security is treated as a platform responsibility, not an optional feature.

#### Authentication and Token Scoping
The platform operates two identity planes:

- Tenant administration via the hub for tenant and shop management

- Shop-specific buyer identities for B2B and authenticated shop usage

We enforce the following:

- Token-based authentication for all privileged APIs

- Tenant admin tokens scoped to the tenant context and administrative roles

- B2B buyer tokens scoped to the shop context and buyer roles

- Strict separation between control plane and shop APIs

- No privilege escalation between identity planes

- Short-lived access tokens and controlled refresh mechanisms

Public shop browsing requires no authentication and remains isolated from administrative endpoints.

#### Logical Tenant Boundaries
Tenant isolation is enforced at the application, query, and cache layers.

We enforce:

- Mandatory shop ID resolution before any data access

- Strict query filtering by shop identifiers

- Cache keys scoped to the shop and locale context

- No cross-tenant read access by design

- Automated tests to detect scope violations

Physical per-tenant database isolation is not implemented in the MVP. Escalation of isolation via shard-level routing is supported without requiring an architectural redesign.

#### Network and Runtime Isolation
Runtime isolation protects critical services.

We enforce the following:

- Workloads deployed in isolated Kubernetes clusters, per environment

- Network segmentation between public ingress, internal services, and data stores

- Private connectivity to PostgreSQL, Redis, Service Bus/Event Hub, and AI Search

- No public exposure of internal data services

- Strict ingress routing via Azure Front Door and WAF

Runtime services are stateless to prevent cross-request contamination. Administrative endpoints are protected by stricter network and identity controls than public shop traffic.

#### Artifact Validation and Signing
Themes and extensions are treated as controlled artifacts.

We enforce the following:

- Immutable, versioned artifacts for themes and extensions

- Validation checks prior to publication

- Compatibility checks against declared API and rendering contracts

- Capability-based permission declarations for extensions

- Controlled publication exclusively via the control plane

Themes and extensions must not:

- Execute backend business logic

- Access databases directly

- Make arbitrary outbound network calls

- Override routing or SEO identity rules

The platform reserves the right to disable or quarantine artifacts that compromise stability or security.

#### WaWi Monitoring and Observability
Operational transparency and governance traceability are required to operate the platform securely and investigate incidents.

We enforce the following:

- Administrative actions are logged with the identity of the executor, a timestamp, the scope of affected resources, and the outcome of the action

- Changes to tenant and shop configuration are auditable

- Theme publication, rollback, and version binding actions are auditable

- Extension installation, activation, update, deactivation, and removal actions are traceable

- Changes to roles and permissions are traceable

- Security-relevant events such as repeated authentication failures, permission violations, and activation of extension kill switches are traceable

Audit records are collected centrally and retained in accordance with platform governance policies.

Audit and observability logs are subject to the retention policies defined by platform governance. Retention periods may vary depending on the sensitivity and operational relevance of the recorded data.

We enforce the following:

- Audit records are read-only and protected against uncontrolled modification

- Audit logs support reconstruction of governance actions and operational incidents

- Audit data visibility is restricted according to administrative and operational roles

In addition to governance traceability, the platform provides operational observability for runtime components.

We ensure:

- Centralized logging, metrics collection, and distributed tracing across runtime services, data stores, and event consumers

- Monitoring of cache performance, database utilization, and event processing lag as first-class operational indicators

- Alerting on sustained increases in error rate, infrastructure utilization, or abnormal access patterns

Audit logs are treated as governance artifacts and remain separate from the operational telemetry used for performance monitoring and troubleshooting.

### 8.18 Operating Model and Scalability
This section describes how the platform is deployed, operated, monitored, and scaled. The MVP is designed to operate in a single Azure region and has a clearly defined development path toward multi-region resilience. The operational design emphasizes predictable behavior, controlled scaling, and cost governance.

#### Single-Region MVP Architecture
The MVP operates in a single Azure region.

We enforce the following:

- All runtime workloads are deployed in a primary region

- Multi-AZ deployment within the region for high availability

- Managed database with zone redundancy enabled

- Redis deployed with a high-availability configuration

- Azure AI Search deployed with a replica configuration aligned to expected load

The single-region model simplifies:

- Deployment topology

- Operational complexity

- Incident response procedures

- Cost predictability

The platform remains fully multi-tenant within the region. Cross-region failover is not implemented in the MVP.

#### Evolution Path to Warm Standby
The architecture supports evolution toward a warm standby model for multiple regions.

We enforce the following:

- Infrastructure-as-Code enabling deployment of a secondary region

- Geo-replication capability for databases via Azure PostgreSQL

- A replication strategy for AI Search aligned to the regional model

- Configuration replication across regions through control plane automation

Characteristics of the warm standby model:

- Secondary region provisioned with minimal runtime capacity

- Traffic redirection via Azure Front Door in the event of primary region failure

- Failover time in the range of minutes, not hours

Active-active multi-region is not planned in the initial roadmap due to:

- Data consistency complexity

- Operational overhead

- Increased cost burden

Evolution toward higher resilience is carried out in a controlled, incremental manner.

**Figure 7: Single-Region MVP Architecture**

#### Autoscaling and Capacity Planning
Compute scaling is designed to be horizontal from the ground up.

We enforce the following:

- Kubernetes Horizontal Pod Autoscaling based on CPU and request metrics (using KEDA)

- Predefined minimum scaling thresholds for baseline availability

- Upper scaling limits to protect cost boundaries

- Manual pre-scaling for anticipated traffic spikes such as seasonal campaigns

Database scaling is governed by:

- Vertical scaling as the primary mechanism

- Read replicas where justified by load

Search scaling is governed by:

- The number of replicas is adjusted based on query load

- Index partitioning is adjusted to business volume growth

Capacity planning is data-driven and reviewed on a regular basis. The platform does not rely on uncontrolled automatic scaling as a substitute for architecture.

**Figure 8: Autoscaling Overview**

#### Monitoring and SLO Strategy
Operational transparency is mandatory.

We enforce the following:

- Centralized logging via Azure Monitor

- Distributed tracing via Application Insights

- Metrics collection across runtime, database, cache, search, and event consumers

- Event backlog and projection lag monitoring as first-class indicators

Service level objectives are defined for:

- Shop availability

- API latency percentiles

- Event processing lag

- Error rate thresholds

An alert is triggered on:

- Sustained increase in error rate

- Cache degradation

- Database saturation

- Event backlog exceeding defined tolerance threshold

Operational metrics are reviewed regularly within the framework of platform governance. Operational monitoring and alerting rely on the observability infrastructure described herein.

#### Infrastructure Cost Control
Infrastructure costs are treated as a controllable variable, not an afterthought.

We enforce the following:

- A cache-first strategy to minimize backend compute load

- Resource tagging by environment and service class

- Regular cost reviews against traffic baselines

- Autoscaling caps to prevent uncontrolled expansion

- Clear separation between production and non-production costs

Cost increases must correlate with:

- Increased traffic

- Increased tenant volume

- Increased catalog size

Cost deviations without correlation to traffic are treated as operational anomalies. The platform architecture explicitly avoids compute-intensive designs where caching can achieve equivalent results.

### 8.19 Architectural Constraints and Non-Goals
This section defines the explicit architectural boundaries of the platform. These constraints are deliberate design decisions. They prevent uncontrolled complexity, safeguard performance guarantees, and ensure platform stability. Features or behaviors outside these boundaries require an architectural review and alignment with the roadmap.

#### Synchronization and Consistency Boundaries
The platform operates on an eventual consistency model for read operations. We enforce the following:

- No real-time synchronization guarantees with JTL-WaWi in the MVP

- Defined tolerance for projection delays in catalog, price, and inventory views

- Event-driven updates instead of synchronous WaWi read operations.

The shop is not a transactional system of record.

We explicitly do not:

- Replicate the full WaWi transactional logic in the shop

- Store authoritative order status independently of WaWi

- Guarantee zero-latency catalog synchronization

Transactional correctness is ensured at checkout by confirmation from the WaWi system.

#### Personalization and Caching Constraints
Performance depends on caching discipline.

We prescribe:

- Public HTML must remain cacheable by shop and locale

- Currency, region group, and B2B context must not fragment CDN HTML caching

- Personalization is performed only in authenticated or API-bound flows

We explicitly do not:

- Support fully personalized public HTML at the edge layer

- Allow dynamic price variants to generate SEO-identical duplicates

- Allow extensions or themes to cause uncontrolled cache key variations

Cache fragmentation is treated as an architectural violation.

#### Execution boundaries for extensions and themes
Themes and extensions operate within strict execution boundaries.

We mandate:

- Presentation logic exclusively in themes

- Capability-based permissions for extensions

- No arbitrary code execution at runtime

- No direct database access by extensions or themes.

We explicitly do not:

- Allow plugins to override core routing or SEO identity rules

- Allow extensions to bypass API contracts

- We do not permit runtime mutation of published artifacts

Platform governance takes precedence over unrestricted extensibility

#### Availability and multi-region constraints
The MVP will operate in a single Azure region.

We enforce the following:

- High availability across multiple AZs within the region

- Warm standby as a first step toward improving failover resilience

We explicitly do not offer:

- Active-active multi-region in the MVP

- Zero-downtime guarantees during regional outages

- Cross-region write consistency

The messaging backbone is configured in an active-passive model across regions. Event production and consumption occur in a single active region during normal operations. Failover to the secondary region requires an explicit promotion action, which can be triggered manually or automatically via operational runbooks. Consumers in the secondary region remain passive until failover is initiated. Higher availability tiers require roadmap planning and cost alignment.

#### Roadmap boundaries and future development
The architecture supports evolution, but not uncontrolled expansion.

We enforce the following:

- Isolation escalation via shard routing when required

- Warm-standby region as a milestone for failover resilience

- Structured extension and growth of the theme ecosystem

We explicitly do not:

- Pursue unlimited feature parity with all global e-commerce platforms in the MVP

- Introduce uncontrolled feature layering that compromises performance guarantees

- Blur the boundaries of responsibility between the shop and WaWi

Future features are prioritized based on:

- Platform stability

- Operational feasibility

- Cost viability

- Business alignment

Architectural integrity takes precedence over the pace of feature development.

## 9 Implementation of JTL Shop 6.0 and MVP
The realization of Shop 6.0 begins with an MVP. This builds on the technical infrastructure and will be progressively and flexibly expanded.

The technical infrastructure is based on Microsoft Azure. The architecture follows a modular, scalable design and comprises the following core components:

- Provisioning of an Azure subscription with dedicated resource groups for development, testing, and production

- Setup of a Kubernetes environment (AKS) for orchestrating frontend and middleware components

- Configuration of Azure App Services, Azure Functions, and Azure Storage for middleware, caching, and static content

- Provisioning of Azure Key Vault for secure management of API keys and credentials

- Connection of the on-premises JTL-WaWi to the WaWi cloud or API gateway layer via a secured connection (e.g. Azure VPN Gateway)

- Implementation of monitoring and logging solutions (Azure Monitor, Application Insights) to oversee API usage, availability, and performance

This infrastructure forms the technical foundation for deploying the MVP and enables later scaling to additional shops and regions. The MVP delivers a first production-ready JTL Shop 6.0 that reliably maps core commerce processes and enables legally compliant operation for Germany and the EU. At the same time, it specifically addresses the most significant limitations of the current Shop 5.0 model that restrict time-to-value, operational reliability, and economic scalability in day-to-day use. The focus is on multi-shop operations, centralized data management in JTL WaWi, and a seamless end-to-end workflow from catalog and availability through checkout and payment to order creation and fulfillment. Features include the connection of a first shop frontend, the integration of JTL-WaWi as the central data source for products, inventory, customers, and orders, the implementation of a complete checkout process including payment connectivity (e.g. PayPal, credit card), and the synchronization of orders and inventory between the shop and WaWi. The implementation of core functions such as product display, shopping cart, customer account, and shipping options, as well as the framework for multi-shop functionality, round this out.

This creates a starting point that enables early sales, customer feedback, and validation of the platform logic under real-world conditions. Additional capabilities will be added to this foundation in a structured manner, without breaking the core logic. The target scope also includes AI-assisted features that relieve merchants operationally and support data-driven optimizations, without undermining the data and process authority of the WaWi core. Further extensions include expanded multi-tenancy (multiple merchants per instance), additional sales channels (e.g. marketplaces, POS), advanced marketing and CRM features (e.g. personalized coupon management), and the integration of a cloud version of the WaWi.

### 9.1 Features and MVP scope
The prioritization of functional requirements and the definition of the MVP focus on the essential core functions.

The MVP described below represents the current proposal for a functionally and technically sound first expansion stage of JTL Shop 6.0. It serves as a reliable reference for implementation, but should not be understood as an immutable final specification. In the course of further project refinement, the MVP scope can and should be further refined in line with detailed technical concepts, dependencies, implementation risks, and prioritized business requirements.

With the delivery of this MVP, JTL receives a first production-ready Shop 6.0 release with core logic and functionality. This includes in particular a shop frontend, the integration of product, inventory, pricing, customer, and order data via JTL-WaWi, a functional customer account, checkout with shipping and payment connectivity, and the structured transfer of orders to WaWi for further processing. In addition, the MVP already includes the foundation for multi-shop operations with centralized management of multiple frontends, the maintenance and reuse of templates and frontend elements, and initial AI-assisted support in shop design — particularly for style definition and layout configuration in the theme builder. This establishes a platform foundation on which real sales, customer feedback, and the structured expansion of additional capabilities can be built.

"Relevant for MVP" features are functions that can be defined as the minimum necessary level of meaningful usability. These include, for example, multi-shop capability, centralized data management, end-to-end order processing, and functional shop frontends, as well as customer management and similar capabilities. Extended "Shop 6.0 Must-have" features such as comprehensive B2B or marketing functionality will follow in later expansion stages and represent the currently expected competitive landscape.

|**Feature / Requirement**|**Description**|**Shop 6.0**<br>**"Must**<br>**Have"**|<br>**Relevant**<br>**for MVP**|
|---|---|---|---|
||**Centralized product maintenance**<br>Products, variants, and categories are maintained centrally. Master data, prices, inventory, and category assignments are managed centrally;<br>the lead system is JTL-WaWi, so the shop requires no duplicate data maintenance.|||
||**Automated data synchronization**|||
|**Central article management**|An automated sync regularly and reliably transfers product data, categories, inventory, prices, and status changes from the ERP system to the<br>online shop. Changes in JTL-WaWi are reflected in the shop in a timely manner.|**Yes**|**Yes**|
||**Consistent data foundation**<br>Centralized control produces a uniform, low-error data foundation. Variant logic, availability, and assortment changes are consistently managed<br>from WaWi and correctly displayed in the shop.|||
||**Centralized maintenance in WaWi (lead system)**<br>JTL-WaWi remains the leading system for all customer-related master data. Customer data, addresses, customer groups, and debtor information<br>are managed primarily in WaWi and serve as the authoritative data source for the online shop.<br>**Automated data synchronization**<br>An automated sync reliably transfers customer and debtor data between WaWi and the shop. New customers, changes to master data, or<br>address updates are synchronized in a timely manner and displayed as current in the shop.|||
|**Central customer management**|**Data editing in the customer account**<br>Customers can edit certain data in the shop, such as addresses or contact details. These changes are transferred back to WaWi via the<br>synchronization process and maintained there centrally.|**Yes**|**Yes**|
||**Consistent data foundation**<br>The consistent lead-system principle of WaWi produces a unified, consistent dataset for the shop, order processing, and internal processes.<br>Duplicate maintenance is avoided and sources of error are reduced.|||
||**Identity & security**<br>Customers can register and log in, forgot-password process, multi-factor authentication, social login (e.g. Google/Apple).<br>**Master data & preferences**|||
|**Customer account**|Customers can manage and edit their information. Address book (billing and delivery address), profile, newsletter settings, preferred payment<br>method, account deletion (GDPR).|**Yes**|**Yes**|
||**Transaction & interaction history**<br>Order overview, shipment tracking, order history,|||

|**Display of product**<br>**relationships**|**Featured products & recommendations**<br>Support for upselling and cross-selling lists. The shop can display automatically generated product lists based on user behavior and AI-assisted<br>recommendation mechanisms.<br>**Manual control**<br>Shop managers can manually influence or override recommended products.<br>**Accessory and relationship logic**<br>Display of accessories, alternatives, and further product relationships; support for complex, multidimensional taxonomies.|
|---|---|
|**Product configurator**|**Attribute-based product configuration**<br>Products can be configured based on defined attributes (e.g. color, size, material). The selection dynamically updates variants, prices, or images.<br>**Valid combinations & rules**<br>Dependencies between attributes are taken into account so that only valid configurations can be selected. Price rules can be defined.<br>**WaWi-compatible data structure**<br>All configuration data is transferred to WaWi in a structured and unambiguous manner (including attribute values, variant identifiers, and pricing<br>logic) to ensure correct further processing in WaWi.|
|**Bundle logic**|**Creating product bundles**<br>Combining multiple products into a package (e.g. set items, accessory bundles, quantity packages). Discount options.<br>**Attribute and variant support**<br>Bundles can consist of variant items or attribute-based configurations.<br>**Structured WaWi transfer**<br>All bundle components are transferred individually and correctly to the WaWi/WaWi structure — including quantities, variants, and prices.|
||**Synchronization of inventory and availability**<br>Inventory and availability data are regularly synchronized between WaWi and the shop to reliably display current stock levels and/or availability.|
|**Central**<br>**inventory**<br>**management**|**Prevention of overselling**<br>The sync ensures that only available quantities are offered in the shop. Inventory changes from WaWi are adopted in a timely manner.<br>**Yes**<br>**Yes**|

|**Inventory**<br>**management**|**Reservation and buffer functions**<br>The shop supports reservations during the ordering process as well as configurable inventory buffers to prevent bottlenecks and incorrect<br>fulfillment.|**Yes**||
|---|---|---|---|
||**Inventory & availability**<br>Display options for available inventory and/or availability status for products and variants. Configuration options per product: continue selling at<br>≤0 availability or mark as non-inventory-tracked.|||
|**Inventory & availability**<br>**display**|**Delivery time at product level**<br>Display of the estimated delivery time on product listings and the product detail page.<br>**Address-based delivery time calculation**<br>Calculation of the actual delivery time after the delivery address is entered at checkout.|**Yes**|**Yes**|
|**Inventory &**<br>**availability display**|**Pre-order function**<br>Products can be pre-ordered when order quantity > availability. Maintenance of estimated delivery time and quantity, split-delivery option.|||
|**Regional requirements DE**|**Tax and legal logic**<br>Regional tax rules and legally compliant price display are structurally supported and set by default. Reduced tax rates and tax-exempt products<br>are possible.<br>**Legally compliant display of information**<br>Local requirements for mandatory disclosures and notice texts are observed, including data protection, withdrawal button, and legal notice.<br>**Price display**<br>Display of gross prices in B2C shops, unit price calculation, and display of the legally required unit price (e.g. €/kg, €/l, €/m) for transparent<br>pricing.|**Yes**|**Yes**|
|**Regional requirements DE**|**Integrated consent manager**<br>An integrated consent manager enables legally compliant collection and management of consents for cookies, tracking services, and third-party<br>tools. Settings can be adjusted in the admin.<br>**Regional payment and shipping methods**<br>Support for established local payment methods and shipping options, including country-specific settings.|<br>**Yes**||
|**Regional requirements EU**<br>**Internationalization**|**Analogous to DE, EU only**<br>**International localization**<br>Support for full localization of language, currency, taxes, shipping terms, and content. Language and country selection in the frontend,<br>configurable per market.|**Yes**<br>**Yes**||

#### Multiple Markets
Multiple markets can be served either via dedicated shops or through a single shop frontend with market-specific configurations (prices, taxes, product range, shipping terms, content).

#### Taxes
Configuration of input tax for CH and GB, integration of OSS with automatic tax calculation, tax exemptions, reduced tax rates

#### Shop Admin
Support for multiple languages in the shop administration, at minimum DE and EN

#### Customer-Specific Pricing Logic
Support for customer-specific prices, price lists, tiered pricing, and individual pricing and shipping terms.

#### Extended Customer and Company Model
B2B accounts with company structure, including company contact, multiple users, and roles/permissions.

#### Individual Shop Views
B2B customers can receive their own customized shop view. Certain products or content can be displayed or made available for purchase exclusively to selected customers or customer groups.

#### Control Price Visibility
#### B2B Logic
Prices can be hidden from non-logged-in visitors (including Google indexing) to support B2B negotiations or protected pricing structures.

**Shipping and Delivery Terms per Customer or Customer Group**

Individual shipping methods, shipping costs, and delivery terms can be defined per B2B customer or customer group.

#### Requested Delivery Date
Customers can specify a preferred delivery date during the ordering process; this is passed to the WaWi/ERP processes.

#### Payment Terms
Support for B2B-specific payment terms such as cash discount, payment targets, or restricted payment methods.

#### Quick Order
Input forms for article numbers (SKUs) as well as CSV uploads for fast bulk orders.

#### B2B Features
#### Order Lists & Templates
Creation of order lists, saving of shopping carts, order templates, and reorder functions for frequently needed items.

#### Quotation Function
Ability to create, request, or accept quotes — within the customer account.

#### Sales Document Overview
Display of all relevant documents such as delivery notes and invoices directly in the B2B customer account. Documents can be searched and sorted by date, number, amount, or status. All documents are available for download (e.g. PDF). **Packaging Units (PU)** Support for different packaging units such as carton, pallet, or set. Order quantities can be automatically adjusted to the defined PU. Packaging units such as carton, pallet, or set. Order quantities can be automatically adjusted to the defined PU. **Units of Measure**

Sales in various units of measure possible (e.g. piece, linear metre, litre, square metre) including automatic conversion logic.

#### Real-Time Stock Levels
Binding display of availabilities in the shop, multiple warehouses possible, rule set for prioritized warehouses or cumulative display.

#### Detailed Product Information
Provision of technical data sheets, CAD drawings, assembly instructions, and packaging content information directly on the product detail page **B2B Information** and on a download page. **Customer Account: Order History & Document Download**

Access to past orders, invoices, delivery notes, delivery status, and shipment tracking — including download functionality.

#### B2B Payment Methods
Support for typical B2B payment methods such as purchase on account, SEPA direct debit, or restricted payments — controllable by customer group or via dynamic rules. **VAT ID Validation** Automatic verification of the VAT ID upon registration of B2B customers.

**Additional B2B Functions B2B Catalog View** Clear tabular presentation of product lists with relevant attributes and attribute values for quick navigation of large product ranges. Quick-buy function for direct product purchasing from the list view.

#### Access to Pages or Areas
Certain areas or individual pages of the shop can be unlocked for specific customers or groups. Password protection for specific pages is also possible.

||**Management of CMS Elements and Templates**<br>Central control of all page templates, CMS building blocks, and design variants. Frontend elements can be duplicated, published, and reused —<br>including inheritance logic for content and settings.|||
|---|---|---|---|
|**Theme Management**|**Theme Settings**<br>Central maintenance of global theme settings such as colors, fonts, spacing, and global design parameters.|**Yes**|**Yes**|
|**Shop Frontend:**<br>**Basic Page Templates**|**Product List/Category Pages (PLP)**<br>Ready-to-use standard templates for category and list views (e.g. SERP), including grid/list view and sorting.<br>**Product Detail Page (PDP)**<br>Ready-to-use standard templates with sections for product information, images, variants, price, availability, and call-to-action elements.<br>**Additional Standard Pages**<br>Ready-to-use templates for shopping cart, checkout, customer account, legal texts/CMS pages, thank-you page, and 404 page.|**Yes**|**Yes**|
|**Shop Frontend:**<br>**Basic Content Elements**|**Predefined Content Elements**<br>The shop is delivered with a set of frontend elements, e.g. sections and blocks for texts, images, teasers, or combined content.<br>**Page Design**<br>The content elements can be placed on and combined with page templates to build content quickly and consistently and display it in the theme<br>layout. Multiple different page templates are possible.<br>**Header and Footer**<br>Standardized header and footer elements for navigation, search field, logo, contact, or footer links that are ready to use and customizable.|**Yes**|**Yes**|
|**Shop Frontend:**<br>**Basic Widgets**|**Standard Widgets**<br>The shop is delivered with a set of ready-to-use widgets, including breadcrumb, announcement banner, slider, and custom overlays.<br>**Interactive Overlays**<br>Integrated overlay for shopping cart preview for direct user interaction.|**Yes**||
|**Shop Frontend:**|**Flexible Page Design**|||
|**Content Elements and Widgets**|Content elements can be freely placed, combined, and flexibly arranged on pages (drag & drop).|||

|**Shop Notifications**|**Additional Message Formats (possibly nice-to-have?)**<br>Push notifications, SMS service, WhatsApp|**Yes**|
|---|---|---|
|**Search, Sorting, Attributes**|**Search Function & Indexing**<br>The shop features a fast search function with indexed product data. The search finds products, categories, and content pages.<br>**Sorting & Filter Basics**<br>Standard sorting options (e.g. price, relevance, new arrivals) are available and can be used in the shop frontend.<br>**Attribute and Category Display**<br>Product attributes and categories are clearly presented in the frontend and support quick orientation for users.|**Yes**<br>**Yes**|
|**Advanced Search, Filters**|**Advanced Search Functions**<br>Weighting of individual data fields, influence on search result rankings, structured search preview for improving hit quality. Synonyms, blacklist,<br>fault-tolerant search.<br>**Attribute-Based Filter Display**<br>Editing and display of filter options for category pages in the frontend. Different filter sets can be assigned to individual or multiple categories.<br>Grouping of filter values, color swatches.<br>**Custom Product Lists**<br>Creation of shop product lists manually or by rule set, e.g. for landing pages, campaigns, or topic-specific pages. Shop product lists can be<br>independent of product categories in the WaWi.||
||**Simple Discount Logic**<br>Support for shop discounts such as discount codes or promotions that can be set up directly in the shop admin.||
|**Marketing: Discounts**|**Display of Shop and WaWi Discounts**<br>Both discounts assigned in the shop and product discounts from the WaWi are displayed correctly.<br>**Clean Order Data Integration**<br>Discount information is captured in a structured manner in the order data so that correct assignments in JTL-WaWi are possible.|**Yes**|
|**Customer Retention**|**Gift Voucher Handling**<br>Support for gift vouchers, including creation, redemption, and management in the shop and in the WaWi.<br>**Wish List Function**<br>Customers can save products to a wish list; saved items are stored in the customer account.<br>**Product Comparison**<br>Customers can display comparable products directly on the PDP to find the most suitable product.||

|**Extensions and Embedding of**<br>**Third-Party Apps**|**Integration of Apps and Themes**<br>The shop supports the straightforward installation of third-party apps and themes that provide feature extensions for the frontend and/or backend.<br>Third-party providers are given access to all required interfaces and information.<br>**Seamless Frontend Extensions**<br>Frontend extensions integrate automatically into existing theme styles and settings without affecting other areas (no side effects).<br>**Easy Installation for Shop Operators**<br>Apps can be installed and managed directly in the admin to add additional features quickly and reliably.<br>**Building an Extension Framework for Connection to the App Store and Partner Platform (subject to availability)**<br>Apps can be technically configured, developed, activated, and purchased in combination with the app store, etc.|<br>**Yes**|
|---|---|---|
|**Integration of AI Assistance for**<br>**Merchants**<br>**AI Assistant "Build"**|**AI Assistant in the Shop**<br>An integrated AI assistant supports merchants as a consultant and agency. Support with setup, operation, and optimization of the shop — from<br>initial configuration through content creation to process automation. The assistant is accessible from anywhere in the shop (shop admin, theme<br>management, theme editor).<br>**AI-Assisted Theme Setup**<br>Support in building the shop theme, including creation of the theme style as well as design and layout settings.<br>**AI-Assisted Frontend Build**<br>Support in creating frontend elements and populating target-group-optimized content, including creation of page templates and widgets.<br>**Shop Backend Configuration**<br>AI assistance with core settings in the shop admin such as taxes, shipping costs, notifications, activating payment methods in the checkout, and<br>installing apps.|**Yes**<br>**Yes**|
|**Integration of AI Assistance for**<br>**End Customers**|**Technical Foundation for AI Features**<br>The shop provides the basis for AI-powered features such as recommendation engines, shopping assistants, or comparable visitor features.<br>**Extensible in Later Phases**<br>AI features for end customers will follow in a later phase (Phase 2) and can be added easily.<br>**Integration Point for Third-Party Providers**<br>The architecture enables third-party providers to integrate their own AI modules seamlessly and to build on existing data structures.|**Yes**|

**Table 19: Feature Overview**
### 9.2 MVP Estimate
The following estimate for the MVP provides a rough overview of the technical effort required to implement the MVP scope described in this proposal.

The estimate is organized by functional area and technical responsibility and covers frontend development, backend services, infrastructure setup, DevOps automation, and quality assurance measures.

The scope includes the core platform features such as storefront runtime and rendering infrastructure, WaWi integration with JTL-WaWi, catalog and order synchronization, multi-shop architecture, theme and page builder functionality, payment and shipping integration, search and product discovery, AI-powered tools, and the required cloud infrastructure. Effort is stated in person-days and covers development work exclusively.

The following estimate includes a 20% buffer to account for risks and uncertainties, including bug fixing, unexpected requirement changes, integration issues, performance optimization, edge cases, refactoring, deployment adjustments, and additional testing.

Legend: FE: Frontend, BE: Backend, DO: DevOps, QA: Quality Assurance, AI: AI-Architect

|**Area**|**Epic**|**Task**|**FE**|**BE**|**DO**|**QA**|**AI**|
|---|---|---|---|---|---|---|---|
|||Define frontend structure, routing, and layout system|5|||||
||Define System|Define service architecture, API boundaries, and DB schema||5||||
||Architecture|Define runtime architecture and CI/CD model|||4|||
|**Ahitt**||Define test strategy||||4||
|**rcecure**||Define component library and UI blocks|5|||||
||Component and<br>Itf Di|Define API contracts and DTOs||3||||
||nerace esgn|Define environment topology|||3|||
|||Create test plan||||3||
|||Configure FE deployment pipeline|3|||||
||Azure|Integrate services with infrastructure||5||||
||Environment<br>|Set upAzure RG, networking, AKS, Redis, OpenSearch|||6|||
|**Infrastructure**|Setup|Validate environments||||1||
||CI/CD Pili|FE build pipeline|2|||||
||penes|Backend build pipeline||2||||
|||Implement configuration UI|2|||||
|**Platform**|Shop<br>Configuration|Implement configuration service||2||||
|||Set upconfiguration storage|||2|||
|||Implement product display|3|||||
||Catalog|Implement catalog sync service||7||||
||Synchronization|Configure integration connectivity|||3|||
|||Test sync process||||1||
|**WaWi**||Design WaWi connector abstraction||3||2||
|**Integrati**|WaWi Connector<br>Laer|Implement connector interface||3||2||
|**on**|y|WaWi Connector Layer||23||||
|||Implement WaWi event ingestion||6|4|2||
||WaWi Events|Event mappingto internal domain||7||2||
|||Retry/failure handling||2|2|1||

||Product|Implement projection DB schema||3|2|
|---|---|---|---|---|---|
||Projection<br>Storage|Create projection updater||5||
|||Set up payment environment||1||
||Payment UI|Paymentgatewayintegration||3||
||Integration|Payment selection at checkout|3|||
|**Pt**||Test payment workflow|||1|
|**aymen**||Handle payment result UI|1|||
||Payment Status|Webhook handling&payment events||2||
||Sync|Monitor payment events||1||
|||Test payment flow|||1|
|||Implement PLP/PDP pages|4|||
||Ctl P|Product API endpoints||3||
||aaog ages|FE hosting configuration||2||
|**Storefront**||UI tests|||2|
|||Account pages UI|2|||
||Customer Account|Customer API endpoints||2||
|||Test customer account|||1|
||Predefined<br>Extensions/App<br>s|Creation of predefined extensions/apps (e.g. cookie consent)|4|2|1|
||Inventory|Reservation logic during checkout|2|2|2|
||Reservation|Reservation release logic||3|1|
|||Customer account UI integration|1|||
||Customer|Customer sync service||3||
|**Commerce**<br>**Core**|Synchronization|Monitor integration jobs||1||
|||Test customer sync|||1|
|||Displayinventorystatus|1|||
||Inventory|Inventory sync logic||4||

||Synchronization|Set upmonitoringfor sync jobs||3||
|---|---|---|---|---|---|
|||Verifyinventoryconsistency|||1|
|||Implement cart UI and checkout pages|2|||
||Cart &|Implement cart service and checkout logic||2||
||Checkout|Configure checkout services||1||
|||E2E tests checkout|||2|
|||Checkout submission UI|1|||
|**Orders**|Order Creation|Implement order creation service||2||
|||Monitor order services||1||
|||Test order lifecycle|||1|
|||Display order status in account|1|||
||Order Sync to|Implement WaWi order sync||4||
||WaWi|Monitor sync jobs||1||
|||Validate WaWi sync|||1|
|||Implement shipping selection UI|2|||
||Shipping|Implement shipping logic||2||
||Methods|Configure shipping integration||1||
|**Shiin**||Test shipping|||1|
|**ppg**||Displayshippingstatus|1|||
||Fulfillment|Implement shipment update service||2||
||Synchronization|Monitor fulfillment jobs||1||
|||Test shipment status updates|||1|
|||Implement template editor UI|23|||
||Theme Builder|Theme storage & config APIs||23||
||Foundations|Set upasset storage||3||
|**Builder**||Test builder|||3|
|||Implement drag/drop editor, section controls, block placement UI|14|||

|Page Builder UI|Create APIs for storing layouts and a builder schema||14||
|---|---|---|---|---|
||Validate builder editing workflows and regression tests|||3|
||Create template editor UI and template selection screens|9|||
|Template System|Implement CRUD, version management, and assignment APIs for<br>templates||9||
||Test template flows for create/edit/apply|||2|
||Implement reusable block components and block configuration panels|23|||
|Block Component<br>System|Implement block configuration model and rendering configuration APIs||5||
||Test block rendering and configuration persistence|||3|
||Create UIs for creating, editing, listing, and publishing pages|5|||
|Page Management|Implement CRUD and publish APIs for pages||5||
||Test page lifecycle flows|||1|
||Develop the media library UI, upload flow, and selection modal|9|||
|Media Asset<br>|Implement media APIs and asset references||14||
|Management|Configure blob storage, access rules, and delivery path||3||
||Test upload/selection/render flows|||2|
||Create theme selection and customization UI|14|||
|Theme<br>Management|Implement theme service and theme bindings||23||
||Test theme assignment and preview flows|||3|
||Dashboard UI|7|||
|Shop Dashboard|Dashboard APIs||5||
||Test dashboard|||2|
||AI content UI|7|||
|AI Content Tools|AI integration services||19|5|
|**AI**<br>|Configure AI services||4|5|
||Test AI workflow|||3<br>3|

||AI Agent|Development/Training||||20|
|---|---|---|---|---|---|---|
|||Search UI and filters|4||||
|**Sh**|Sh Itf|Search indexingandqueries||4|||
|**earc**|earc nerace|Configure search infrastructure||2|||
|||Test search|||1||
|||FE developer docs|1||||
|**Documentatio**<br>**n**|Delivery<br>Documentation|Backend architecture docs||1|||
|||Infrastructure documentation||1|||
|||Integrate frontend with rendering contracts and preview behavior|4||||
||SSR Rendering<br>|Implement rendering service and SSR orchestration||7|||
||Service|Configure runtime scaling and deployment for renderer||6|||
|||Validate rendered output and SSR behavior|||3||
|||Implement FE integration for rendering rules of templates/blocks|4||||
|**Rendering**|P Rdi||||||
||age enerng<br>Pipeline|Implement render pipeline for page, layout, and data hydration||6|||
|||Test rendering correctness across all page types|||1||
|||Create preview mode and publish action UX|4||||
||Draft/Publish<br>Lifecycle|Implement draft/publish workflow and content status management||6|||
|||Test preview,publish, and undo flows|||1||
|||Create domain configuration UI and validation feedback|1||||
||Domain<br>Management|Implement APIs for domain management and verification flow||4|||
|||Configure DNS/gateway/front door integration||2|||
|**Routing**||Test domain bind/unbind/resolve flows|||1||
|||Process resolved shop context when bootstrapping the FE app|1||||
||Shop Resolution|Implement host-to-shop resolver service||2|||
|||Configure edge routing rules||1|||

|||Test multi-shop host routing|||1|
|---|---|---|---|---|---|
|||Implement localization-aware routing and UX for locale switching|2|||
||Locale Routing|Implement locale resolution and routing rules||2||
|||Configure CDN/edge routing behavior||1||
|||Test country-specific redirects and routing|||1|
|||ApplyFE cache headers and cache rules to routes|1|||
||CDN Cache|Design cache keys and rules for cache eligibility||6||
||Strategy|Configure CDN/Front Door caching rules||4||
|||Validate cache hit and miss behavior|||1|
|||Implement Redis cachingforprojections / render data||2||
|**Cachin**|Redis Caching|Deploy and configure Redis||1||
|**g**||Test cache consistency and fallback|||1|
|||Trigger expected UI updates after publish/update|1|||
||Cache Invalidation|Implement an invalidation service for changes to content, products, and<br>shops||5||
|||Configure purge hooks / CDN invalidation||4||
|||Test invalidation correctness|||1|
|||Build the UI for SEO fields for pages/products/templates|9|||
||Metadata<br>Management|Implement metadata service and storage||3||
|||Validate behavior of title, meta tags, and canonical tags|||1|
|**SEO**||Implement frontend URL structure handling|1|||
||Canonical URLs|Implement the logic forgeneratingcanonical URLs||1||
|||Test canonical consistency|||1|
||Sitemap|Implement the sitemap generation service||1||
||Generation|Test sitemap completeness|||1|
|||Implement the login and registration UI|2||1|
|**Customer**<br>**Account &**|Authentication &<br>Sessions|Implement the AuthenticationService and session management||2|1|
|||Configure the authentication environment and security settings||1||

|**Identity**|Customer Profile|Implement the customer profile UI|2|||
|---|---|---|---|---|---|
|||Implement customer profile APIs and persistence||3||
|||Validate profile update flows|||1|
|||Implement account pages and order historyUI|2|||
||Customer Account<br>|Implement customer synchronization with WaWi||3||
||Integration|Monitor synchronization jobs||1||
|||Test account integration and data consistency|||1|
||Guest Order|Guest data handling||4|1|
|||Guest checkout option(UI toggle, flow, validation)|6||2|
|||Implement the notification UI|2|||
||Notification|Implement the notification service and event triggers||3||
|**Notifications**|Service|Configure the notification infrastructure and email provider||2||
|||Test notification delivery and event handling|||1|
||Email Temlates|Implement the email template preview UI|2|||
||p|Implement the template storage and rendering logic||3||
||Bi|Define WCAG baselines + checklist|1|||
||asc<br>Requirements<br>(compliance|Review core flows (home page, product detail page, shopping cart,<br>checkout)|3|||
||with standards)|Semantic HTML + ARIA patterns|2||1|
|||Alt text support (admin + rendering)|1||1|
|**Accessibility**|Perceivability|Contrast handling in the theme (tokens/rules)|1|1|1|
|||Media accessibility (hook for supporting video subtitles)|2|||
||Operability|Keyboard navigation (all key flows)|2||1|
|||Redesign of interactions (no time-critical UX)|1||1|

||Error handling<br>+ support|Accessible error messages (UX + structure)|2|1|1||
|---|---|---|---|---|---|---|
||for screen<br>readers|Structured HTML for screen readers|1||1||
||C Ftilit|Configuration model for analytics|2|2|1||
|**Analytics**<br>**(Basic)**|ore unconay|Admin user interface|4|1|1||
||Event model|Standard events(page,product, cart, checkout)|4|5|2||
|**Total**|||**231**|**301**|**79**<br>**93**|**33**|

**Table 20: Effort Estimates MVP**
The MVP has an estimated scope of approximately 750 person-days of development within the scope defined here. The PO/PM, UI/UX, and Delivery Lead roles are calculated on the basis of the overall project duration, assuming an allocation of 19 working days per month. Governance and steering functions such as PM, PO, and UI creation can be estimated at approximately 300 person-days (PM and PO accompany the project on a permanent basis). The project totals approximately 1,050 person-days.

### 9.3 Team Setup
The following team configurations illustrate alternative delivery timelines. The table shows which roles have an impact on implementation time and how the expected time horizon should be assessed.

|**Role**|**Level**|**_6-month_**|**_9-month_**|
|---|---|---|---|
|**Delivery Lead**|Lead|_100%_|_100%_|
|**Backend**|Senior|_100%_|_100%_|
|**Backend**|Advanced|_100%_||
|**Backend**|Advanced|_50%_||
|**Frontend**|Senior|_100%_|_100%_|
|**Frontend**|Advanced|_100%_||
|**Frontend**|Advanced|_50%_||
|**DevOps **|Senior|_50%_||
|**DevOps **|Junior||_100%_|
|**QA**|Advanced|_100%_||
|**QA**|Intern||_100%_|
|**PO/PM**|Advanced|_75% -100%_|_50%_|
|**UI/UX**|Advanced|_50%_|_50%_|

**Table 21: Team utilization by scenario**

A realistic implementation should plan for approximately 7 months from kickoff to first MVP activation (beta). Hardening can be estimated at approximately 2 months. From around month 5 onward, initial 1st-party extensions could potentially be developed in parallel.

The team roles and competencies are described in the "Appendix: Team Roles".

### 9.4 Roadmap and Milestones
The following overview outlines an initial timeline for the MVP implementation, which will be refined at project start based on the precise PO specifications. The roadmap shows parallel workstreams of an agreed technical foundation, commerce core, storefront, and content/builder features and supplementary platform services.

Each workstream distinguishes between conception, implementation, integration, quality assurance, and hardening. This makes it clear that topics such as architecture, interfaces, WaWi integration, templates, rendering, payment, and operational readiness are largely processed in parallel and progressively merged.

The roadmap is not a rigid process plan, but describes one implementation option for the MVP. What is decisive is the delivery of individual features aligned with a technically integrated, operationally usable, and stabilized overall direction.

**Figure 9: MVP Roadmap – Milestones & Activities**

## 10 Conclusion
This document provides JTL with a strategic, functional, and technical foundation for evaluating the further development of the JTL Shop toward a cloud-capable, modular, and economically scalable multi-shop platform. The target vision thus addresses the key structural weaknesses of the current Shop 5.0 and simultaneously describes how the process strengths of JTL-WaWi can be carried over into a future-proof platform model. This establishes a basis for treating the further development of JTL Shop 6.0 not as a purely technical migration, but as a deliberate product and platform decision.

The MVP elaborated in this document represents a functionally and technically sound starting point for this purpose. It describes a production-ready Shop 6.0 state with clear core logic and prioritizes the features that are relevant early on for usability, operational readiness, and scalability. At the same time, the defined MVP scope should deliberately not be understood as a final commitment. Before implementation, it should be validated and refined jointly with JTL in the next project phase, taking into account functional priorities, detailed technical concepts, dependencies, resource availability, and implementation risks.

The key management decisions encompass the decision in favor of a Shop 6.0 with the described or adjusted positioning, and the confirmation/adjustment of the target corridor for the defined MVP.

The next step based on this decision therefore consists of a focused clarification and planning phase in which the MVP scope, delivery perimeter, team setup, implementation logic, and decision premises are defined. On this basis, the MVP can be refined and tailored so that its realization best meets the functional requirements, the technical framework conditions, and the expectations of JTL and its customers.

Based on the decisions and elaboration of the EPICs, both the budget framework, the team, and the implementation timeline can be further refined.

## Appendix: Challenges and Proposed Solutions
This chapter examines the dependencies and challenges that may arise when operating JTL-WaWi as an on-premises system in a cloud context. It specifically outlines the potential constraints and possible technical obstacles to be considered in order to ensure a stable and secure system landscape. It also shows how these challenges can affect ongoing operations and what measures are recommended to minimize constraints.

### On-Premises Operation of JTL-WaWi in a Cloud Context
1. Availability Risk (WaWi Instance Failure)

   - Since JTL-WaWi is operated locally at the merchant's site, it is susceptible to infrastructure failures (e.g., power outages, server defects, network problems). If WaWi goes down, no product data can be updated, orders processed, or inventory synchronized. This can lead to temporary outages or malfunctions in the connected shops.

2. Connectivity Issues Between Cloud Frontend and On-Premises WaWi Communication between the cloud-based middleware and the locally installed WaWi requires a stable, secure, and performant connection (e.g., via VPN or reverse proxy). Unstable internet connections, firewall conflicts, or misconfigured ports can cause API calls to fail, resulting in shops not receiving current data or orders not being transmitted correctly.

3. Scaling Bottlenecks with a High Number of Shops Since all shops access a single central WaWi instance, performance bottlenecks can occur as the number of storefronts grows, particularly if WaWi is running on hardware not designed for high parallel loads. This can lead to delayed data updates, timeouts, or even system crashes.

4. Maintenance and Update Dependency On-premises systems require regular maintenance, updates, and security patches. If these are not carried out promptly, incompatibilities with the middleware or security vulnerabilities may arise. In addition, a WaWi update can have unforeseen effects on API communication with the shop if interfaces change.

5. Lack of High Availability and Redundancy Unlike cloud services, a locally operated WaWi generally offers no automatic redundancy or failover mechanisms. A hardware defect or a local issue can therefore lead to a complete standstill of shop communication, with direct consequences for revenue and customer satisfaction.

6. Complexity of Root Cause Analysis Since the system architecture is distributed across multiple layers (frontend in the cloud, middleware, on-premises WaWi), root cause analysis for errors can be complex and time-consuming. Without centralized monitoring and logging solutions, there is a risk that problems are detected too late or misclassified.

7. Security Risks from External Connectivity Opening the on-premises WaWi for external access (e.g., via an API interface) entails potential security risks. Without careful protection (e.g., authentication, encryption, access restrictions), unauthorized access or data leaks could occur.

### Sync Load on WaWi
A key challenge when operating JTL-WaWi in a cloud context is the additional load created by continuous synchronization processes. Since all shops retrieve or write back product-, customer-, and order-related data from or to WaWi in near real time, WaWi becomes a central bottleneck. As the number of connected shops or the order volume increases, the frequency of API requests and data retrievals rises accordingly. When overload situations occur, WaWi responds with delays or rejections of API calls (see section 9.2).

The architecture of JTL Shop 6.0 must therefore incorporate mechanisms for load throttling, data buffering, and intelligent query optimization in order to protect WaWi from overload and ensure stable shop communication.

### Schema Changes in the Future PIM
With the planned introduction of a separate PIM system, additional challenges arise for data consistency between PIM, WaWi, and the connected shops. Since the PIM may in future be centrally responsible for product data maintenance, attribute logic, or content enrichment, schema changes in the PIM have a direct impact on downstream systems. New fields, modified structures, or changed validation rules can cause the middleware or the shop to no longer correctly interpret or render the data.

This becomes particularly critical if WaWi and PIM are used in parallel or if the leading system changes per entity. Without clearly aligned data models, there is a risk of inconsistent product information, missing records, faulty variant structures, or content that cannot be rendered in the shop frontend. This can negatively affect both product display and pricing and inventory logic.

To keep the overall architecture stable, schema changes in the PIM must be detected early, versioned, and intercepted in the middleware before they reach the shop. The architecture of JTL Shop 6.0 therefore requires defined contracts, clear responsibilities, and a structured testing and approval process for every change to the data model.

### Proposed Solutions

For the key challenges described above, possible solution approaches exist in connection with the external integration and its effects on the system architecture:

- Use of monitoring and alerting systems for the connection to WaWi: By introducing monitoring and notification systems, the stability of the interfaces to WaWi can be ensured. This allows potential disruptions to be detected early and appropriate measures to be initiated.

- Caching strategies in the middleware to cushion short-term outages: With effective caching mechanisms, data is buffered so as to compensate for temporary outages or delays in WaWi. This preserves shop performance even during interruptions or load peaks.

- Clear escalation and restart processes for WaWi outages: A defined procedure for WaWi outages ensures that critical processes can be resumed quickly and downtime is minimized.

- Medium-term migration of WaWi to the cloud via Azure: Migrating WaWi to a cloud environment such as Azure can provide greater scalability and resilience in the long term and simplify the integration of external systems.

### API Rate Limit of JTL-WaWi
JTL-WaWi has limited capacity for parallel API calls. If the permitted number of requests per time period is exceeded, for example due to heavily frequented shops, multiple simultaneous storefronts, or intensive synchronization processes, WaWi can throttle or reject API requests. This leads to delayed data updates, incomplete product or inventory queries, and potentially erroneous order transmissions. Especially during periods of heightened demand such as campaigns or seasonal peaks, increased API throughput is required to ensure system performance. Recurring breaches of the limit can impair the overall performance of connected shops, cause timeout errors, and significantly degrade the user experience.

### Proposed Solutions

**1.** Use of caching mechanisms in the middleware

   - Frequently requested data (e.g., product lists, categories, prices) is cached so that only a fraction of requests are actually forwarded to WaWi. This substantially reduces API throughput and prevents load peaks on WaWi.

**2.** Request batching and optimization of query frequencies API calls are consolidated (batch requests), unnecessary individual requests are eliminated or executed at intervals. This reduces the number of parallel requests without compromising data freshness.

**3.** Introduction of an API rate limiter in the middleware The middleware itself controls how many requests per second are passed through to WaWi. When the limit is reached, requests are buffered or cached to proactively prevent overload situations.

**4.** Monitoring and alerting for API throughput and error rates Continuous monitoring of API response times, error codes, and request spikes. Early warning notifications enable intervention before the limit is exceeded.

**5.** Reduce read-only load through replication or additional services Where possible, search functions, product data, or price calculations can be handled by outsourced services (e.g. search servers, cache layers) to minimise the number of direct WaWi API calls.

**6.** Scaling the WaWi instance / performance optimisation Under sustained high load, the on-premise WaWi (or a future cloud variant) should be scaled to more powerful hardware, optimised databases, or parallel API workers.

**7.** Planning a medium-term migration of the WaWi to the cloud A cloud deployment of the WaWi enables significantly higher scalability, more stable API response times, and prevents local infrastructure bottlenecks.

### Release cycle of JTL-WaWi
Since JTL-WaWi is developed independently of the cloud-based frontend, changes to API endpoints, data structures, or business logic can have immediate effects on the functionality of the connected shops. If API fields are removed, renamed, or extended without the middleware or frontend being updated in time, this can lead to incorrect product displays, inconsistent stock data, or orders not being transmitted. This is particularly critical when WaWi updates are applied on the retailer side without a

coordinated deployment process, as this can create a temporary incompatibility between backend and frontend. This jeopardises the stability of the shop functions, impairs data quality, and can disrupt the operational running of the entire multi-shop system. To counter these challenges, JTL-Shop 6.0 relies on cloud-based web services that act as a connector between the individual systems.

### Approaches to solutions

1. Define clear version compatibility Frontend, middleware, and WaWi should only be operated in tested and approved version combinations in order to prevent unplanned incompatibilities.

2. Use middleware as an abstraction layer Changes to the WaWi API are first intercepted in the middleware and transformed for compatibility before they reach the frontend. This keeps the frontend stable even when backend structures change.

3. Controlled rollout of WaWi updates Updates to the WaWi should never be carried out in an uncoordinated manner, but rather through defined maintenance windows or coordinated deployments, to ensure the integrity of all connected shops.

4. Early update testing in staging environments New WaWi versions should be tested automatically against the middleware and frontend integrations in order to detect API breaks or data format changes at an early stage.

5. Monitoring for API changes and misbehaviour A central monitoring system captures API errors, changed structures, or unusual response behaviour immediately, so that problems after updates become visible without delay.

6. Versioned APIs and protection against breaking changes Where possible, versioned API routes or stable interface contracts should be established so that changes in the WaWi backend do not propagate directly to the frontend.

### Frontend connector as the central stability layer in the release cycle
The connector forms the technical bridge between JTL-WaWi and the frontend of JTL-Shop 6.0. Since both WaWi and the connector are developed independently, this component must be maintained as a stable, versioned abstraction layer (mapping between frontend model and backend (potentially automatable)). Only in this way can it be ensured that frontend and backend remain compatible despite updates.

Within the release cycle, the frontend connector performs the following tasks:

   - Change reconciliation of the WaWi API: delivery of consistent data models to the frontend, even when backend structures change

- Support for frontend customisations: delivery of consistent data models to JTL-WaWi when the underlying, unified data structure is extended or modified

- As a result, the connector is the cornerstone of compatibility: it protects shop functions from breaking changes on both sides.

To ensure the consistency of schemas and data, the following must be observed when maintaining the Shop 6.0 connector:

1. Clear version management & compatibility definition

   - For each new WaWi or frontend version, it is documented which connector version is compatible.

   - A release is only approved once the connector is able to process the changes.

2. Middleware as a buffer

- Structural and field changes in the WaWi are intercepted and transformed in the middleware before they reach the frontend.

- This keeps the frontend stable even when APIs change in the background.

3. Automated checks

- Contract tests and schema comparisons continuously verify whether WaWi responses still match the expected structures.

- Deviations are detected early and corrected before live updates.

4. Controlled update processes

   - WaWi updates are first tested against the connector in a staging environment.

   - The connector determines whether an update can be activated without risk.

5. Ensuring frontend compatibility

   - Changes to the frontend model (products, categories, checkout structures, etc.) are reflected in the connector.

   - This keeps the frontend functional without requiring direct adjustments to WaWi logic.

In the following section, the functional and technical requirements explained above are translated into a concrete software architecture. This creates a bridge between the general principles and their practical application within the project.

### Proposed AI tools
|Tool|Purpose|Application|
|---|---|---|
|Claude|AI<br>assistant<br>for<br>programming,<br>problem-solving, and<br>structured workflows|<br>Use for brainstorming, implementing features,<br>refactoring, debugging, and documentation;<br>define CLAUDE.md and reusable workflows<br>(skills) for consistent usage|
|Claude Code|AI<br>programming<br>agent for repository-<br>based<br>tasks<br>and<br>workflows|<br><br>Use for implementing features, changes across<br>multiple files, refactoring, debugging, and test<br>generation; define CLAUDE.md and reusable<br>skills for consistent workflows|
|Copilot|Helps developers<br>with coding in the<br>IDE; accelerates<br>implementation and<br>adheres to code<br>conventions|Use in the IDE for inline suggestions and code<br>generation; define copilot-instructions to control<br>behaviour; suited for small to medium tasks and<br>established patterns|

|GPT|General-purpose<br>AI<br>for<br>problem-solving,<br>planning,<br>and<br>text<br>generation<br>Use for breaking down tasks, architecture<br>discussions, documentation, debugging, and<br>ticket creation; use clear prompts and context for<br>better results|
|---|---|
|Codex|Repository-based<br>programming and<br>structured<br>development tasks<br>For changes across multiple files, refactoring,<br>test generation, and documentation updates;<br>define AGENTS.md to control behaviour and<br>constraints|
|CodeRabbit|Automated pull<br>request review and<br>code quality checks<br>Integrate into GitHub PR workflows; configure<br>rules<br>per<br>path<br>(frontend,<br>backend,<br>infrastructure);<br>detect<br>errors<br>and<br>receive<br>improvement suggestions before human review|
|Spec-Kit|Specification-driven<br>development and task<br>generation from<br>requirements<br>Convert specifications into structured tasks and<br>plans;<br>maintain<br>clear<br>and<br>consistent<br>specifications to guide development (can employ<br>other agents for implementation)|
|Gstack|Role-based<br>AI<br>workflow<br>for<br>planning, review, QA,<br>and delivery<br>Use as a structured workflow on Claude Code;<br>invoke<br>roles<br>(e.g.<br>planning,<br>review,<br>QA,<br>delivery); manage development in defined steps<br>rather than ad-hoc prompts|
|Gemini|General-purpose<br>AI<br>for<br>programming,<br>problem-solving, and<br>generation<br>Use like GPT for planning, programming,<br>debugging, and documentation; results depend<br>on prompt quality|
|Rovo (Jira AI|)<br>AI integrated into Jira<br>for task automation,<br>knowledge retrieval,<br>and workflow support<br>Use directly in Jira to create tickets, summarise<br>work,<br>manage<br>the<br>backlog,<br>and<br>support<br>planning;<br>use<br>Rovo<br>Agents<br>to<br>automate<br>workflows and connect knowledge across tools|

## Appendix: Team roles
The table below provides an overview of the various team roles and the competencies required for each. Typical areas of responsibility and accountability are also described so that the requirements and expectations for each role are transparent and comprehensible.

**Junior: A Junior is familiar with basic methods and tools such as agile approaches and delivery platforms. Practical experience is typically gained from initial projects or internships. They work under guidance, take on clearly defined tasks, and continue to develop within the team.**

**Advanced: An Advanced Professional already has in-depth knowledge of roadmap and milestone planning, is familiar with delivery tools, and can independently take responsibility for smaller projects or sub-areas. With several years of experience, they are confident in stakeholder communication and the management of dependencies.**

**Senior: Senior professionals independently manage complex projects, control risks, and communicate confidently with all stakeholders. With technical know-how, they ensure quality, transparency, and scalability in the delivery process.**

**Lead: Leads bear overall responsibility for projects, plan milestones, coordinate teams, and manage risks. They ensure transparency and quality and communicate with all stakeholders; technical know-how for modern platforms and APIs is a prerequisite.**

### Team roles overview
### Responsibilities / areas of accountability Required skills Delivery Lead (Level: Lead)
- Responsible for the end-to-end delivery of the platform across frontend, backend, and infrastructure

- • Defining the delivery scope, milestones, and coordination between parallel workstreams

- • Managing risks related to integration, scalability, and dependencies

- Alignment with stakeholders regarding scope, priorities, and timelines

   - Agile/Scrum methods and delivery tools (Jira, Azure DevOps)

   - • Roadmap and milestone planning for multi-team environments • Stakeholder communication and reporting

   - Risk and dependency management

   - Sound knowledge of: microservices architecture, API-based systems, and cloud-native applications

- Ensuring delivery quality, predictability, and transparency

### Product Owner/Project Manager (PO/PM) (Level: Advanced)
- Define and maintain the product backlog in line with business objectives

- Translating business requirements into clear, testable user stories

- Prioritising features based on value, dependencies, and delivery constraints

- Ensuring functional completeness including edge cases and error scenarios

- Close collaboration with design and development during implementation

- Backlog management tools (Jira)

- • Writing user stories and defining acceptance criteria

- Knowledge of e-commerce (catalogue, checkout, orders)

- • Understanding of API-driven systems

- Data-driven prioritisation (analytics, product metrics)

### UI/UX Designer (Level: Advanced)
- Designing user experiences across storefront, account, and builder interfaces

- Defining and maintaining a scalable design system

- • Ensuring usability across responsive breakpoints and accessibility standards

- Supporting product and development teams with clear design specifications

   - Figma (advanced, including prototypes and design systems)

   - • Responsive design (desktop, tablet, mobile)

   - Accessibility standards (WCAG)

   - UX for complex workflows and configuration interfaces

   - • Experience working with component-based frontend systems

- Iterate UX based on feedback and usability findings

||**Responsibilities / areas of accountability**|**Required skills**|
|---|---|---|
|**Backe**|**nd Engineer (Level: Senior)**||
|•<br>•<br>•<br>•<br>•<br>•|Responsibility for the design and further development of backend services in<br>the core areas (catalogue, orders, payments, WaWi integration)<br>Defining API boundaries and ensuring consistent, scalable service<br>communication<br>Ensuring reliable data synchronisation between WaWi and the platform<br>(including error handling and recovery)<br>Development with a focus on performance and scalability (caching,<br>asynchronous processing, read/write optimisation)<br>Defining observability standards (logging, monitoring, alerting) for all services<br>Review code, mentor engineers, and enforce best practices in development|•<br>Node.js with TypeScript (or equivalent backend stack)<br>•<br>API design and implementation (REST, optional GraphQL)<br>•<br>Database design and optimisation (PostgreSQL or similar<br>relational database)<br>•<br>Event-driven architecture (message queues such as Kafka,<br>Azure Service Bus, or similar)<br>•<br>Caching strategies (Redis)<br>•<br>Authentication and authorisation (OAuth2, JWT, session<br>management)<br>•<br>Containerisation (Docker)<br>•<br>Cloud platforms (preferably Azure: containers, networking<br>fundamentals)<br>•<br>Observability tools (logging, monitoring, tracing)<br>•<br>Experience integrating with external systems (WaWi, payment<br>gateways,or similar)|
|**Backe**|**nd Engineer (Level: Advanced)**||
|•<br>•<br>•<br>•<br>•|Implementing backend services and APIs in accordance with the defined<br>architecture<br>Developing business logic for core functions (catalogue, orders, integrations)<br>Integration with external services and APIs<br>Ensuring code quality through testing and debugging<br>Ensuring system stability through error analysis and troubleshooting|•<br>Node.js / TypeScript (or equivalent backend stack)<br>•<br>Implementation of REST APIs<br>•<br>SQL and database interaction<br>•<br>Background jobs and asynchronous processing<br>•<br>Integration with external APIs<br>•<br>Basic authentication concepts (JWT, sessions)<br>•<br>Unit and integration testing|
|**Fronte**|**nd Engineer (Level: Senior)**||
|•<br>•<br>•<br>•<br>•|Defining the frontend architecture including rendering strategy and routing<br>Building and maintaining scalable component systems and UI architecture<br>Ensuring performance, SEO, and accessibility of the storefront<br>Integrating the frontend with backend APIs and data flows<br>Review code and set standards for frontend implementation|•<br>Next.js (SSR, ISR, routing, middleware)<br>•<br>React (advanced patterns, hooks, state management)<br>•<br>SEO optimisation (metadata, structured data)<br>•<br>Performance optimisation (Core Web Vitals)<br>•<br>Component library design and reusable UI systems<br>•<br>API integration and data fetching strategies|

||**Responsibilities / areas of accountability**|**Required skills**|
|---|---|---|
|**Fronte**|**nd Engineer (Level: Advanced)**||
|•<br>•<br>•<br>•<br>•|Implementing UI components, pages, and features based on design<br>specifications<br>Integrating frontend with backend APIs<br>Ensuring responsive and consistent UI behaviour<br>Handling user input, validation, and UI state<br>Debugging and resolving UI-related issues|•<br>React and Next.js fundamentals<br>•<br>Component-based development<br>•<br>Routing and page structure<br>•<br>REST API integration<br>•<br>Form handling and validation<br>•<br>State management fundamentals<br>•<br>Implementinga responsive user interface|
|**DevO**|**ps Engineer (Level: Senior)**||
|•<br>•<br>•<br>•<br>•|Designing and maintaining the cloud infrastructure for the platform<br>Defining and managing CI/CD pipelines for all services<br>Ensuring system reliability, scalability, and security<br>Managing network, routing, and environment configuration<br>Monitoring system health and resolving infrastructure issues|•<br>Microsoft Azure: VNet, Private Link, DNS; Azure Front Door<br>/ CDN; Key Vault<br>•<br>Kubernetes (AKS): deployment, scaling, configuration<br>•<br>CI/CD tools (Azure DevOps, GitHub Actions)<br>•<br>Docker (advanced)<br>•<br>Infrastructure as Code (Terraform or Bicep)<br>•<br>Monitoring tools (Azure Monitor, logging systems)<br>•<br>Caching systems (Redis, CDN) Application debugging<br>Fundamental understandingof the backend|
|**DevO**|**ps Engineer (Level: Junior)**||
|•<br>•<br>•<br>•|Support with the setup and maintenance of infrastructure<br>Support with the execution and monitoring of the CI/CD pipeline<br>Support with the management of environments and deployments<br>Monitoring of logs and support with troubleshooting|•<br>Basic knowledge of using Azure<br>•<br>Basic Kubernetes operations (deployments, logs)<br>•<br>Use of CI/CD pipelines<br>•<br>Docker fundamentals<br>•<br>Scripting (Bash or similar)<br>•<br>Log monitoring and troubleshooting|
|**Qualit**|**y Engineer (Level: Advanced)**||
|•<br>•<br>•<br>•<br>•|Definition and execution of test strategies across platforms<br>Verification of system behaviour across all integrations (WaWi, payment,<br>shipping)<br>Ensuring the quality of end-to-end user flows (checkout, account, builder)<br>Identifying errors, edge cases, and system inconsistencies<br>Support with release preparation and regression testing|•<br>Test planning and test case design<br>•<br>API testing (Postman or similar tools)<br>•<br>End-to-end testing tools (Playwright or Cypress)<br>•<br>Integration and regression testing<br>•<br>Troubleshooting in frontend and backend systems<br>•<br>Basic understanding of CI/CD|
|**Table 2**|**2: Tasks and skills per team**||

## Appendix: High-Level Request Architecture
## Appendix: Infrastructure Request Flow
## Appendix: Single-Region MVP Architecture
## List of Figures

- Figure 1: High-Level Platform Architecture — p. 44
- Figure 2: Overview of an Infrastructure Request — p. 46
- Figure 3: Context Resolution Model — p. 60
- Figure 4: Routing Resolution Overview — p. 63
- Figure 5: Overview — p. 66
- Figure 6: Event Processing Overview — p. 72
- Figure 7: Single-Region MVP Architecture — p. 77
- Figure 8: Autoscaling Overview — p. 78
- Figure 9: MVP Roadmap – Milestones & Activities — p. 111

## List of Tables

- Table 1: Chapter Logic — p. 4
- Table 2: Quick Reading Paths — p. 4
- Table 3: User and Company Structure JTL-Shop 5.0 vs. 6.0 — p. 8
- Table 4: Business Model & Market Orientation JTL-Shop 5.0 vs. 6.0 — p. 8
- Table 5: Product Range & Operational Complexity JTL-Shop 5.0 vs. 6.0 — p. 9
- Table 6: Technological Stance JTL-Shop 5.0 vs. 6.0 — p. 9
- Table 7: User Expectations & Priorities JTL-Shop 5.0 vs. 6.0 — p. 9
- Table 8: Role of Partners in JTL-Shop 5.0 vs. 6.0 — p. 9
- Table 9: Evolution of E-Commerce Architectures — p. 12
- Table 10: Provider Clusters in the DACH Region — p. 15
- Table 11: Competitive Landscape Overview — p. 16
- Table 12: Platform Layers — p. 45
- Table 13: Task Areas Data vs. Control Plane — p. 46
- Table 14: Technology Stack Overview — p. 48
- Table 15: AI Usage in Development — p. 50
- Table 16: Comparison of Page Types — p. 51
- Table 17: SEO Identity Overview — p. 52
- Table 18: Error Scenarios — p. 72
- Table 19: Feature Overview — p. 100
- Table 20: Effort Estimates MVP — p. 109
- Table 21: Team Utilisation by Scenario — p. 110
- Table 22: Tasks and Skills per Team — p. 122

## List of Abbreviations

| Abbreviation | Meaning |
|---|---|
| bzw. | respectively |
| ebd. | ibid. |
| et al. | and others |
| ggü. | compared to |
| i. d. R. | as a rule |
| n. a. | not applicable |
| o. g. | aforementioned |
| rd. | approx. |
| u. a. | among other things |
| u. ä. | and similar |
| u. v. m. | and many more |
| z. B. | for example |
| zzgl. | plus |
| vs. | versus |

## Bibliography

Dragoni, N., Giallorenzo, S., Lafuente, A. L., Mazzara, M., Montesi, F., Mustafin, R., & Safina, L. (2017). Microservices: Yesterday, today, and tomorrow (arXiv:1606.04036). arXiv. https://doi.org/10.48550/arXiv.1606.04036

EHI Retail Institute. (n.d.). In which areas do you use artificial intelligence (AI)? https://de.statista.com/. Retrieved from https://de.statista.com/statistik/daten/studie/1073476/umfrage/umfrage-zu-einsatzbereichen-fuer-kuenstliche-intelligenz-im-handel-in-deutschland/

Tiwana, A. (2013). Platform Ecosystems: Aligning Architecture, Governance, and Strategy. Morgan Kaufmann Publishers Inc.

Verhoef, P. C., Kannan, P. K., & Inman, J. J. (2015). From Multi-Channel Retailing to Omni-Channel Retailing: Introduction to the Special Issue on Multi-Channel Retailing. Journal of Retailing, Multi-Channel Retailing, 91(2), 174–181. https://doi.org/10.1016/j.jretai.2015.02.005
