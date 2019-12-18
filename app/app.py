import argparse
import csv
import sys
import util

def main():
    """Main entry point for normalize utility.

    Parses CL arguments and initiates the file normalization process.
    """

    parser = argparse.ArgumentParser('Please provide input and output file paths')
    parser.add_argument('inputfile', type=str, help = 'This is an input .csv file path to be normalized')
    parser.add_argument('outputfile', type=str, help = 'This is the normalized output .csv file path')

    args = parser.parse_args()
    
    __NormalizeFile(args.inputfile, args.outputfile)
    #__NormalizeFile('sampledata\sample.csv', 'output2.csv')

def __NormalizeFile(inputfilepath, outputfilepath):
    """Core worflow for parsing an input csv file and writing to output file.

    Takes input and output file paths and parameters. Opens and parses the input file, normalizes
    the contents, and then writes to the output file path.
    """

    with open(inputfilepath, 'r', newline='', encoding='UTF-8', errors='replace') as inputfile:
        filereader = csv.DictReader(inputfile)
        normalizedrows = []
        counter = 0
        # Loop through the input file rows to normalize each one. Only include a row in the
        # output if normalization was successful
        for row in filereader:
            counter += 1
            success, result = __NormalizeRow(row, counter)
            if success: normalizedrows.append(result)

    __WriteNormalizedOutput(outputfilepath, normalizedrows)

def __NormalizeRow(csvrow, counter):
    """Function for normalizing the contents of each row.
    
    If normalization is successful, then returns the normalized row. -> bool, []
    """

    try:
        normalizedrow = []
        __RunNormalization("Timestamp", util.NormalizeTimeStamp, csvrow, normalizedrow, counter)
        __RunNormalization("Address", util.NormalizeText, csvrow, normalizedrow, counter)
        __RunNormalization("ZIP", util.NormalizeZip, csvrow, normalizedrow, counter)
        __RunNormalization("FullName", util.NormalizeFullName, csvrow, normalizedrow, counter)

        # for foo and bar durations, take the floating point decimal return values, combine them, and
        # write the total durection result to the normalized string for the TotalDuration column
        foo = __RunNormalization("FooDuration", util.NormalizeDuration, csvrow, normalizedrow, counter)
        bar = __RunNormalization("BarDuration", util.NormalizeDuration, csvrow, normalizedrow, counter)
        tot = foo + bar
        normalizedrow.append(tot)

        __RunNormalization("Notes", util.NormalizeText, csvrow, normalizedrow, counter)

        sys.stdout.write(f'{",".join([str(x) for x in normalizedrow])}\n')
        sys.stdout.flush()
        return True, normalizedrow

    except Exception as err:
        sys.stderr.write(f"WARNING: Failed to Normalize Row: {counter}, Message: {err}. It will be excluded from output;\n")
        sys.stderr.flush()
        return False, None

def __RunNormalization(column, normalizefunc, inputrow, outputrow, counter):
    """Takes in a Normalization Function and processes a row column value.

    Normalization function must have a delegate signature of (bool, object) = func(string). If successful,
    then the result value is added to the normalized row. Returns the normalized result value, if applicable.
    """

    success, result = normalizefunc(inputrow[column])
    if success:
        outputrow.append(result)
        return result
    else:
        sys.stderr.write(f"WARNING: Failed to Normalize Row: {counter}, Field: {column}, Message: {result}. It will be excluded from output;\n")
        sys.stderr.flush()
        return None

def __WriteNormalizedOutput(outputfilepath, normalizedrows):
    """Write Normalized rows to the output file path.
    """

    with open(outputfilepath, 'w', newline='', encoding='UTF-8') as outputfile:
        filewriter = csv.writer(outputfile, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        filewriter.writerow(['Timestamp','Address','ZIP','FullName','FooDuration','BarDuration','TotalDuration','Notes'])
        filewriter.writerows(normalizedrows)
    
    sys.stdout.write('outputdata.csv created...')
    sys.stdout.flush()

if (__name__ == '__main__'):
    """Call main function if this is the primary point of entry
    """
    main()
