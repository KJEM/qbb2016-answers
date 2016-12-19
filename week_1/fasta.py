class FASTAReader( object ):
    def __init__( self, file ):
        self.file = file
        self.last_ident = None
        

            

    def next( self ):
        if self.last_ident is None:
            line = self.file.readline()
            assert line.startswith( ">" ), "Not valid fasta"
            ident = line[1:].rstrip( "\r\n" )
        else:
            ident = self.last_ident
            
        sequences = []
        while True:
            line = self.file.readline()
            if line == "":
                break
            if line.startswith(">"):
                self.last_ident = line[1:].rstrip( "\r\n" )
                break
            else:
                sequences.append( line.strip() )
        def __len__( self ):
              return len( self.file )
              if len( sequences ) == 0:
                  raise StopIteration
        
        sequence = "".join( sequences )

        return ident, sequence
        
    def __iter__( self ):
        return self