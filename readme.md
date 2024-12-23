See https://github.com/ericoc/utilities/




# ⚡ Energy Table 🔌
The Philadelphia energy utility ("PECO") website
allows for a residential account holder to download an export of their energy usage
in "comma-separated values" (CSV) file format.

---

## Export
The default export file from PECO is named based upon the dates exported,
and contains data such as the following:
> `peco_electric_usage_interval_data_Service 1_1_2023-07-04_to_2023-07-04.csv`

The CSV begings with a header, containing account information, that is ignored:
> ```
> Name,WILLIAM PENN
> Address,"1 S BROAD ST, PHILADELPHIA PA 19112"
> Account Number,1776xxxxxx
> Service,Service 1
> ```

Finally, the file contains a meaningful header, with values including
kilowatt-hours (kWh) of electricity used:
> ```
> TYPE,DATE,START TIME,END TIME,USAGE (kWh),NOTES
> Electric usage,2023-07-04,00:00,00:59,0.29
> Electric usage,2023-07-04,01:00,01:59,0.34
> Electric usage,2023-07-04,02:00,02:59,0.34
> Electric usage,2023-07-04,03:00,03:59,0.32
> ```

## Work In Progress
There is more to come once a database schema is decided...

---

### Examples (TODO)
- https://electric.ericoc.com/
