Populate directory with historical data from the last year:

    $ while read line; do echo $line; ./get_stock_data.sh $line; done < stock_list

Perform a check:

    $ ls *.csv
    AMP.csv	BHP.csv	CBA.csv	FGL.csv	NAB.csv	ORG.csv	RIO.csv	TLS.csv	WDC.csv	WOW.csv
    ANZ.csv	BXB.csv	CSL.csv	MQG.csv	NCM.csv	QBE.csv	SUN.csv	WBC.csv	WES.csv	WPL.csv

TODO
====

1. Create trading strategy framework (parameters: upper and lower bound) - store model(s) in separate flat files.
2. Read in model
3. Create 1000 random points (entry points) across the data time scale [current - 1yr:current]
4. For each entry point, across each stock, determine success/failure. Success: where upper bound is reached before lower bound.
5. Return results (ratio of success vs failures for each stock; something showing correlation in time)
