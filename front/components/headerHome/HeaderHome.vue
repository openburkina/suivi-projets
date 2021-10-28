<template>
  <section class="innerHeadersection">
    <header class="headerClass">
      <div class="headerContainer">
        <nav class="mainNav">
          <span class="headerLogo">
            <a target="_blank"
              ><img src="../../assets/images/logo.png" alt="UNDP Logo"
            /></a>
          </span>
          <span class="projectTitle">Transparency Portal</span>
          <span class="dateUpdatedMobile">Data last updated on:</span>
          <button class="hamburger">&#9776;</button>
          <ul class="navBar false menuinactiveClose">
            <li class="closeWrapper"><button class="menuClose"></button></li>
            <li class="navbarLink searchMobile">
              <div class="searchMobileWrapper">
                <span class="searchIcon"></span
                ><input class="searchBar" placeholder="Search" />
              </div>
            </li>
            <li class="navbarLink"><a href="/">Home</a></li>
            <li class="navbarLink">
              <a class="active" href="/projects">Projects</a>
            </li>
            <li class="navbarLink"><a href="/donors">Donors</a></li>
            <li class="navbarLink">
              <a href="/sustainable-development-goals"
                >Sustainable development goals</a
              >
            </li>
            <li class="navbarLink">
              <a class="" href="/our-approaches">OUR APPROACHES</a>
            </li>
            <li class="navbarLink">
              <div class="dropdown">
                <a class="dropbtn"> MORE</a>
                <div class="dropdown_content">
                  <a class="dropDownItems" href="/about-us/open"> ABOUT US</a>
                  <a class="dropDownItems">Download</a>
                </div>
              </div>
            </li>
          </ul>
          <section class="innerBanner">
            <div class="linkHeading">
              <span>Projects</span><span class="subTitle"></span>
            </div>
          </section>
        </nav>
      </div>
    </header>
    <section class="bannerSection">
      <section class="headerContainer">
        <div class="overviewWrapper">
          <h1>UNDP Transparency Portal</h1>
          <p class="summary">
            In UNDP, we are committed to eradicating poverty, fighting climate
            change and reducing inequalities and exclusion around the world.
            Discover how, with the help of our partners, we work day to day to
            make this a reality.
          </p>
          <div class="searchItems">
            <input
              type="text"
              name="search"
              id="search"
              class="searchField"
              placeholder="Search using Projects, Donors, Recipients or Keyword"
              value=".."
            />
            <a><span class="searchIcon"></span></a>
          </div>
        </div>
        <!-- <YearSummary /> -->
      </section>
    </section>
    
  </section>
</template>

<style lang="scss">
@import '../../style/helpers/_variables';
@import '../../style/helpers/_mixins';
@import 'style';
</style>