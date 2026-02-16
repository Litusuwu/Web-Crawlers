# TikTok

## Prerequisites

The steps to obtain a **Client Key** and **Client Secret**, which are required items to access any API, are:

> Sign up on the TikTok Dev website

> Create an organization (or individual)
>>![Create organization](/imgs/SS7.png)

> Go to 'Manage Apps' and create an App
>>![Developer Portal](/imgs/SS8.png)
>>![Create App](/imgs/SS9.png)

> After creating the App, you will need to apply for TikTok review for approval depending on which API we want to access. The questions are:

> Basic information 
>![Basic Information](/imgs/SS10.png)
Basic information 2
>![Basic Information](/imgs/SS11.png)
> App review (Describe the product and a demo)
>![App Review](/imgs/SS11.png)
> Products (APIs your app needs)
>![Products](/imgs/SS13.png)
> Products example 
> ![Example 1 Products](/imgs/SS14.png)
> Products example 2
>![Example 2 Products](/imgs/SS15.png)


### <u>Research API:</u>

It is an API aimed at the academic community, and quite restricted to it; it is not intended for enterprises because it goes through a rigorous selection process. Similar to Reddit, you have to submit a ticket with the application/research to be performed and wait for a response from the TikTok team before you can start using the API, which also provides moderate rate limits.

* **Ref:** https://developers.tiktok.com/doc/research-api-get-started?enter_method=left_navigation.

The steps are:

* Apply to the Research API through a request following the prerequisite steps
* Once your request is approved by TikTok, a research client will be generated for you. In it you will be able to see all the projects/apps/research approved by TikTok for the Research API; each one is associated with a **Client Key** and **Client Secret** that will be required to connect to the Research API endpoints.
* Once you have these two, you can generate a **Client Access Token** with which you will have access to the Research API.

>>>![TK Instructions Basic](/imgs/SS16.png)

* The estimated time to receive a response for the Research API is <u>4 weeks or 1 calendar month.</u>

* The requirements are right below; considering that Fuzzy will do web scraping and will profit from it, it is very likely that it will not be possible or that they will not accept it into TikTok's research program (also, Fuzzy is not a researcher as such)

>>> ![TK Instructions](/imgs/SS6.png)


### <u>Display API</u>

This API is not for Fuzzy's use case, because it mainly works with OAuth for self-profile; to display information or posts from your own profile. This seems primarily made for promoting yourself on a landing page or for content creator social diffusing; a use case can be seen as in the following image:

![TK Display Information](/imgs/SS17.png)

If in the future we wanted to use this, the procedure is the same as in **Prerequisites**, but you specify **Login Kit** in the **Products** section.

## Data Portability API & Commercial Content API

Same case as Display API; it is out of scope. It is used to transfer data such as names and usernames between TikTok and third-party applications with authorization from the account owner, it is not in scope for Fuzzy, since Fuzzy seeks to discover keywords and browse the web.

On the Commercial Content API side, the only real use case is to evaluate the ads that exist. This could be useful, but also not, since it does not cover the scope of what Fuzzy is designed for.

## Personal Thoughts

After reviewing the documentation for TikTok's official APIs and carefully reviewing its T&Cs; TikTok does not approve the use of any API (Research API included) to scrape, whether for surveillance or commercial use. If it is for profit, it will not allow scraping.

## What TikTok says about Web Scraping

![TK Statement 1](/imgs/SS18.png)
![TK Statement 2](/imgs/SS19.png)

**TK explicitly prohibits "automated scripts to collect information".**

## TikTokApi : David Teather

This is a repository that is viable due to its constant updates. It is open source and has a beneficial update frequency considering that its last update was very recent (February 11). This is mainly because TikTok has one of the most complex and well-implemented anti-bot systems.

It is based on simulation with a headless web browser in Playwright. This is good mainly because it runs the JS engine to generate the signatures TikTok requires; but at the same time, running a web browser per request consumes a lot of compute resources, considering it is Chromium (high RAM and CPU usage).

Also it has a documentation about how to use the repository code, its extensive and complex in a technical level, this is because of the nature of TK anti-bot system.

![Docs OpenSource](/imgs/SS20.png)

The `davidteather/TikTok-Api` repository (V7.2.2 – Feb 2026) is still technically viable thanks to:
	•	Mandatory use of Playwright (real browser automation).
	•	Advanced session management (SessionFactories).
	•	Native proxy integration (ProxyProviders).
	•	Concurrency via asyncio.

However:
	•	Requires real execution of TikTok's JS engine.
	•	Depends on dynamic signatures: msToken, X-Bogus, X-Gnarly.
	•	High CPU and RAM consumption.

Required architecture (minimum viable)

A monolithic script like the one in the repository is not viable. You need:

```
FastAPI (control API)
        ↓
Redis (broker)
        ↓
Celery workers (Playwright)
        ↓
Signature microservice (X-Bogus)
        ↓
Smart proxy layer
```

Key elements:

Celery with --max-tasks-per-child to avoid memory leaks.
Browser Contexts instead of full instances.
Distributed rate limiting (Token Bucket).
Mixed proxy pool (residential + mobile).
Exponential backoff for retries.
Monitoring with Flower + structured logging.

Asynchronous operations are needed mainly because all of this would run slowly, with latencies ranging from 3–10 seconds depending on the profile, because the repository has to load tracking scripts and, when simulating inside a web browser, you must wait for dynamic rendering (TikTok's infinite scroll nature).

It is important to keep in mind that TikTok implements one of the most advanced API protection systems in the tech industry. It focuses on 3 parameters: **msToken**, **X-Bogus**, and **X-Gnarly**. If these values are not provided in the request, TikTok sends an instant 403 error. **msToken** is a login token that validates the legitimacy of an interaction (user session); it has been found that this token rotates every 14 seconds, which quickly invalidates static sessions. **X-Bogus**: TikTok uses a Virtual Machine (VM) written in JavaScript and highly obfuscated that runs in the browser. This VM takes the full URL, the User-Agent, and other environment data (such as screen resolution or device fingerprint) to generate the X-Bogus value. **X-Gnarly** is an additional protection layer that often appears in the headers of HTTP requests, complementing X-Bogus.

Regarding legal terms, it is the same as with Reddit or IG, since there are several cases such as (hiQ vs LinkedIn, TikTok vs Garland) with lawsuits over data scraping, regardless of whether the tool is open source or private; in the European Union as well, there are fines of 200,000 euros for scraping without notification (CNIL 2025).

Due to the complexity involved in scaling a well-functioning TikTok API solution, it is recommended to first evaluate third-party service options before planning an architecture that supports more than 100,000 users with this open-source solution for Fuzzy.

