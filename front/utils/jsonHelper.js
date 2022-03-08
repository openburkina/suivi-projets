const getYears = (data) => {
  return [...new Set(data.map((x) => x.year))].sort()
}

const getRegions = (data) => {
  return [...new Set(data.map((x) => x.region))]
}

const getSectors = (data) => {
  return [...new Set(data.map((x) => x.sector))]
}

const getOrganisations = (data) => {
  return [...new Set(data.map((x) => x.organisation))]
}

const status = (stat) => {
  if (stat == null || stat <= 0) return 'Términé'
  else return 'En cours'
}

const getSeries = (year, tabStatus, data) => {
  let val = [];
  tabStatus.map((stat) => {
    const da = data.find(
      (x) => status(x.activity_status) == stat && x.year == year
    );
    if (da) val.push(da.count);
  });
  return val;
};
const getStatus = (data) => {
  return [...new Set(data.map((x) => status(x.activity_status)))];
};

const styleTitle = (text) => {
  return {
    text: text,
    align: "center",
    style: {
      fontSize: "16px",
      fontWeight: "bold",
      color: "#269ffb",
    },
  };
};


export const amountsStatus = (data) => {
  let tab = [];
  const status = getStatus(data);
  getYears(data).map((year) => {
    let val = {
      options: {
        labels: status,
        title: { ...styleTitle(year) },
      },
      series: getSeries(year, status, data),
    };
    tab.push(val);
  });
  return tab;
}

const regionFilter = (data, region, year) => {
  let val = 0
  data.map((d) => {
    if (d.region == region && d.year == year) {
      val = parseInt(d.sum)
    }
  })
  return val
}

const sectorFilter = (data, sector, year) => {
  let val = 0
  data.map((d) => {
    if (d.sector == sector && d.year == year) {
      val = parseInt(d.sum)
    }
  })
  return val
}

const organisationFilter = (data, organisation, year) => {
  let val = 0
  data.map((d) => {
    if (d.organisation == organisation && d.year == year) {
      val = parseInt(d.sum)
    }
  })
  return val
}
const regionSeries = (data) => {
  let tab = []
  getRegions(data).map((region) => {
    let value = { name: region }
    let temp = []
    getYears(data).map((year) => {
      let sum = regionFilter(data, region, year)
      temp.push(sum)
    })
    value = { ...value, data: temp }
    tab.push(value)
  })
  return tab
}

const sectorSeries = (data) => {
  let tab = []
  getSectors(data).map((sector) => {
    let value = { name: sector }
    let temp = []
    getYears(data).map((year) => {
      let sum = sectorFilter(data, sector, year)
      temp.push(sum)
    })
    value = { ...value, data: temp }
    tab.push(value)
  })
  return tab
}

const organisationSeries = (data) => {
  let tab = []
  getOrganisations(data).map((organisation) => {
    let value = { name: organisation }
    let temp = []
    getYears(data).map((year) => {
      let sum = organisationFilter(data, organisation, year)
      temp.push(sum)
    })
    value = { ...value, data: temp }
    tab.push(value)
  })
  return tab
}

export const amountsOrganisations = (data) => {
  return {
    categories: getYears(data),
    series: organisationSeries(data),
  }
}

export const amountsSectors = (data) => {
  return {
    categories: getYears(data),
    series: sectorSeries(data),
  }
}

export const amountsCoutries = (data) => {
  return {
    categories: getYears(data),
    series: regionSeries(data),
  }
}

export const nameCountriesWithAmount = (montants, regions) => {
  let mt = { ...montants }
  mt.series.map((serie) => {
    const region = regions.find((region) => region.region_code === serie.name)
    serie.name = region.name
  })
  return mt
}
