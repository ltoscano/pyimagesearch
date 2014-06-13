import numpy as np

class Searcher:
	def __init__(self, index):
		self.index = index

	def search( self, queryFeatures ):
		results = {}

		for( k,features ) in self.index.items():
			# compute the chi-squared distance between the features
            # in our index and our query features -- using the
            # chi-squared distance which is normally used in the
            # computer vision field to compare histograms
			d = self.chi2_distance( features, queryFeatures )

			results[k] = d

		#sort the results
		results  = sorted( [ (v,k) for (k,v) in results.items() ] )

		return results

	def chi2_distance( self, histA, histB, eps = 1e-10 ):

		d = 0.5* np.sum( 
			[( 
				( a-b ) ** 2 ) / (a+b+eps)
				for (a,b) in zip(histA,histB)
			] )

		return d
