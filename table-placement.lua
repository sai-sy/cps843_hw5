function Table(tbl)
  tbl.longtable = false
  tbl.longTable = false
  if tbl.attr == nil then
    tbl.attr = pandoc.Attr()
  end
  tbl.attr.attributes["position"] = "H"
  return tbl
end
