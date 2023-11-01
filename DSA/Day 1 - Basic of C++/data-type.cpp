// Platform : Coding Ninjas
// Problem : https://www.codingninjas.com/studio/problems/data-type_8357232
// Language : C++
// Followed AtoZ DSA Sheet by Striver

int dataTypes(string type) {
	if ( (string)type == "Integer" || (string)type=="Float" ) {
		return 4 ;
	} else
	if ( (string)type=="Long" || (string)type=="Double" ) {
		return 8 ;
	} else {
		return 1 ;
	}
}
