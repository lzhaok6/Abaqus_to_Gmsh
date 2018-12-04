// Abaqus_to_Gmsh.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h> 
#include <iostream>
#include <fstream>
#include <string>
#include <locale>
#include <sstream>
#include <vector>
#include <algorithm>

//This code is used to translate Abaqus input file (mesh) exported from BOLT to Gmsh format
//The first commit

//User instructions:
//get rid of the excessive *Elset. 
//Only applies to hexahedral element (AC3D8R)

int main()
{

	/*
	int debug = 0; 
	int i, j, k;
	std::string filename;
	//std::cout << "input the file name here: " << std::endl;
	//std::getline(std::cin, filename, '\n');
	filename = "Fluidcolumn_0.25fthex.inp";
	std::ifstream infile;
	infile.open(filename);
	if (!infile) {
		std::cerr << "cannot open the file" << std::endl;
		exit(1);
	}
	//std::ofstream outFile;
	//outFile.open("output.msh"); //output Gmsh file
	std::vector<std::vector<std::string>> output;
	std::string csvLine;
	int ct = -1;
	std::vector<int> sidesets_start;
	std::vector<int> sidesets_end;
	int nodestart = 0;
	int nodeend = 0;
	int elestart = 0;
	int eleend = 0;

	while (getline(infile, csvLine))
	{
		ct = ct + 1; //the current line number (starting from 0)
		std::istringstream csvStream(csvLine);
		std::vector<std::string> csvColumn;
		std::string csvElement;
		// read every element from the line that is seperated by commas
		// and put it into the vector or strings
		while (getline(csvStream, csvElement, ','))
		{
			csvColumn.push_back(csvElement);
		}
		output.push_back(csvColumn);
		if (csvColumn[0] == "*NODE" || csvColumn[0] == "*Node") {
			nodestart = ct + 1; //the node starts from the next line
		}
		if (csvColumn[0] == "*ELEMENT" || csvColumn[0] == "*Element") {
			//nodeend = ct - 3; //the line where the node definition ends
			nodeend = ct;
			elestart = ct + 1; //the line where element definition starts
		}
		if (csvColumn[0] == "*ELSET" || csvColumn[0] == "*Elset") {
			sidesets_start.push_back(ct + 1); //the line where sidesets (physical group) definition starts
			if (sidesets_start.size() == 1) {
				eleend = ct;
			}
		}
		if (csvColumn[0] == "*SURFACE" || csvColumn[0] == "*Surface") {
			sidesets_end.push_back(ct - 1); //the line where sidesets (physical group) definition ends
		}
		if (ct % 10000 == 0) {
			std::cout << ct << std::endl; //output which line is being read
		}
	}
	//search back to find where exactly does the node definition ends and redefine the value of nodeend. 
	//check if the first string of the line has a number in it. If so, this is the line we are looking for. 
	int flag = 0; 
	while (flag == 0) {
		for (i = 0; i < output[nodeend][0].size(); i++) {
			if (isdigit(output[nodeend][0].at(i))) {//check if the corresponding character in the first string is a digit
				flag = 1; 
			}
		}
		if (flag == 0) {
			nodeend = nodeend - 1;
		}
	}
	//search back to find where exactly does the element definition ends and redefine the value of element
	flag = 0;
	while (flag == 0) {
		if (output[eleend].size() == 1 + 8) {
			flag = 1;
		}
		if (flag == 0) {
			eleend = eleend - 1;
		}
	}
	int NNODE = nodeend - nodestart + 1; //total node number
	int NEL = eleend - elestart + 1; //total element number
	double** GCOORD; //the vector to store the coordinate of nodes
	GCOORD = new double*[NNODE];
	for (i = 0; i < NNODE; i++) {
		GCOORD[i] = new double[3]; 
	}
	int**IEN; //element connectivity matrix
	IEN = new int*[NEL];
	for (i = 0; i < NEL; i++) {
		IEN[i] = new int[8]; 
	}

	double xoffset = 0.0;
	double yoffset = -1.144;
	double zoffset = 0.0;
	if (xoffset != 0 || yoffset != 0 || zoffset != 0) {
		std::cout << "Do you really want to use a non-zero offset?" << std::endl; 
	}

	for (i = nodestart; i < nodeend + 1; i++) {
		GCOORD[i - nodestart][0] = stod(output[i][1]) + xoffset;
		GCOORD[i - nodestart][1] = stod(output[i][2]) + yoffset;
		GCOORD[i - nodestart][2] = stod(output[i][3]) + zoffset;
	}

	for (i = elestart; i < eleend + 1; i++) {
		for (j = 0; j < 8; j++) {
			IEN[i - elestart][j] = stoi(output[i][j + 1]); //change the string to integer
		}
	}

	//Store sidesets (physical group) elements
	int num_sidesets = sidesets_start.size();
	std::vector<std::vector<int>> ien_py;
	for (i = 0; i < num_sidesets; i++) {
		std::vector<int> sideset_column;
		for (j = sidesets_start[i]; j < sidesets_end[i] + 1; j++) { //lines corresponding to the physical group i 
			//if (output[j].size == 3 && sidesets_end[i] == sidesets_start[i]) { //the element number is expressed as initial,end,internal way (only one line is used) 
			if (sidesets_end[i] == sidesets_start[i]) { //the element number is expressed as initial,end,internal way (only one line is used) 
				for (k = stoi(output[j][0]); k < stoi(output[j][1]) + 1; k += stoi(output[j][2])) {
					sideset_column.push_back(k);
				}
			}
			else {
				for (k = 0; k < output[j].size(); k++) { //store all members (k) in the line
					sideset_column.push_back(stoi(output[j][k]));
				}
			}
		}
		ien_py.push_back(sideset_column); //Each sideset_column represents one physical group
	}
	*/

	const char* filename = "C:/Users/lzhaok6/OneDrive/CASE_MESH/DDG_1ftstructuredhex_fs_150m_10m_24m.inp";
	FILE *fp = fopen(filename, "r");
	if (!fp) {
		printf("Cannot open the mesh file");
		system("PAUSE ");
	}

	int N = 1; 
	int NINT = N + 1; 
	std::vector<int>numele_py; //total number of element in each physical group
	int elenode3D = 0;
	int elenode2D = 0;
	elenode3D = NINT*NINT*NINT;
	elenode2D = NINT*NINT;

	char buf[1000];
	do {
		fgets(buf, 1000, fp); //read line by line
	} while (!strstr(buf, "*Node"));
	double a, b, c;
	int d, e, f, g, h, i, j, k, l;
	std::vector<double> VX;
	std::vector<double> VY;
	std::vector<double> VZ;
	int ct = 1;
	while (fscanf(fp, "%*d, %lf, %lf, %lf", &a, &b, &c) != 0) {
		VX.push_back(a);
		VY.push_back(b);
		VZ.push_back(c);
		ct += 1;
		if (ct % 10000 == 0) {
			std::cout << "node: " << ct << std::endl; //output which line is being read
		}
	}
	int NNODE = VX.size();
	//Find *Element to begin storing the element connectivity matrix
	do {
		fgets(buf, 1000, fp); //read line by line
	} while (!(buf[0] == '*'&& buf[1] == 'E' && buf[2] == 'l'));
	//start storing element connectivity matrix
	std::vector<int> EToV;
	ct = 1;
	while (fscanf(fp, "%*d, %d, %d, %d, %d, %d, %d, %d, %d", &d, &e, &f, &g, &h, &i, &j, &k) != 0) {
		EToV.push_back(d);
		EToV.push_back(e);
		EToV.push_back(f);
		EToV.push_back(g);
		EToV.push_back(h);
		EToV.push_back(i);
		EToV.push_back(j);
		EToV.push_back(k);
		ct += 1;
		if (ct % 10000 == 0) {
			std::cout << "element: " << ct << std::endl; //output which line is being read
		}
	}
	//start searching for element sets (FSI_fluid or NRB) 
	std::vector<int> wt_py; //the physical group corresponds to wetted surface
	std::vector<int> nrb_py; //the physical group corresponds to nrb surface
	std::vector<std::vector<int>> ien_py; //the elements in each physical group
	std::vector<std::string> py_surface;
	std::string surf;
	ct = 0;
	//loop until the end of file
	while (!feof(fp)) {
		do {
			fgets(buf, 1000, fp); //read line by line and find *Elset and *Surface definition
			if (feof(fp)) {
				break;
			}
		} while (!((buf[0] == '*' && buf[2] == 'l' && buf[3] == 's') || (buf[0] == '*' && buf[2] == 'u' && buf[3] == 'r')));
		//search for the keyword FSI_fluid or NRB in the char arrary
		std::string currentline(buf); //convert the char array to string to search the key words
		std::vector<int>py_ele;
		if (currentline.find("FSI_fluid") != std::string::npos || currentline.find("NRB") != std::string::npos) { //found the definition element set for FSI_fluid
																												  //If this line is a surface definition, we store the surface face definition for each FSI_fluid pysical group
			if ((buf[0] == '*' && buf[2] == 'u' && buf[3] == 'r')) {
				std::cout << "Have you make the element set sequence in surface definition consistent with the element set definition?" << std::endl;
				system(" PAUSE");
				//put surface definition
				int setnum;
				if (currentline.find("FSI_fluid") != std::string::npos) {
					setnum = wt_py.size();
				}
				else {
					setnum = nrb_py.size();
				}
				for (int i = 0; i < setnum; i++) {
					fgets(buf, 1000, fp);
					std::string haha(buf);
					py_surface.push_back(buf);
				}
			}
			else {
				//store all the elements in this element set (BCIEN) 
				while (fscanf(fp, "%d,", &d) != 0) {
					py_ele.push_back(d); //store all the element number in the current physical group
				}
				if (py_ele.size() == 3) { //the elements are defined in a concise way (e.g., 1,100,1 meaning 1 to 100 with interval 1)
					for (int i = 0; i < (py_ele[1] - py_ele[0]) / py_ele[2] - 3; i++) { //(py_ele[1] - py_ele[0] + 1) is the total number of element
						py_ele.push_back(py_ele[0] + (3 + i) * py_ele[2]); //py_ele[2] is the increment interval
					}
					py_ele[1] = py_ele[0] + py_ele[2]; py_ele[2] = py_ele[1] + (py_ele[1] - py_ele[0]);
				}
				if (currentline.find("FSI_fluid") != std::string::npos) {
					wt_py.push_back(ct);
				}
				else {
					nrb_py.push_back(ct);
				}
				numele_py.push_back(py_ele.size());
				ct += 1;
				ien_py.push_back(py_ele);
			}
		}
	}
	//extract the element surface information and store the IEN and BCIEN matrices 
	std::vector<std::string>surface;
	for (int i = 0; i < py_surface.size(); i++) {
		ct = 0;
		std::stringstream ss(py_surface[i]);
		while (ss.good()) {
			std::string substr;
			getline(ss, substr, ',');
			if (ct == 1) { //only store the second string
				substr.erase(std::remove(substr.begin(), substr.end(), '\n'), substr.end());
				substr.erase(std::remove(substr.begin(), substr.end(), ' '), substr.end());
				surface.push_back(substr);
			}
			ct += 1;
		}
	}
	std::cout << " " << std::endl;

	//define IEN
	int NEL = EToV.size() / elenode3D;
	int **IEN = new int*[elenode3D];
	for (int i = 0; i < elenode3D; i++) {
		IEN[i] = new int[NEL];
	}
	for (int i = 0; i < NEL; i++) {
		for (int j = 0; j < elenode3D; j++) {
			IEN[j][i] = EToV[i*elenode3D + j];
		}
	}
	double** GCOORD = new double*[NNODE];
	for (int i = 0; i < NNODE; i++) {
		GCOORD[i] = new double[3];
	}
	for (int i = 0; i < NNODE; i++) {
		GCOORD[i][0] = VX[i];
		GCOORD[i][1] = VY[i];
		GCOORD[i][2] = VZ[i];
	}

	//write Gmsh output file
	std::ofstream outfile;
	outfile.open("output.msh");
	if (!outfile) {
		std::cerr << "cannot open the file" << std::endl;
		exit(1);
	}
	outfile << "$MeshFormat" << std::endl;
	outfile << "2.2 0 8" << std::endl;
	outfile << "$EndMeshFormat" << std::endl;
	outfile << "$Nodes" << std::endl;
	//write nodes
	outfile << NNODE << std::endl;
	for (int i = 0; i < NNODE; i++) {
		outfile << i + 1 << " " << GCOORD[i][0] << " " << GCOORD[i][1] << " " << GCOORD[i][2] << std::endl;
	}
	outfile << "$EndNode" << std::endl;
	//write elements (based on physical groups)
	outfile << "$Elements" << std::endl;
	//derive the total elements to be written in the file (in all physical groups)
	int totalele = 0;
	int num_sidesets = wt_py.size() + nrb_py.size(); 
	for (int i = 0; i < num_sidesets; i++) {
		totalele += ien_py[i].size();
	}
	totalele += NEL;
	outfile << totalele << std::endl;
	ct = 1;
	for (int i = 0; i < num_sidesets; i++) { //different physical groups (3 stands for quad element)
		for (int j = 0; j < ien_py[i].size(); j++) { //loop through each element in the physical groups
			outfile << ct << " " << 3 << " " << 2 << " " << i + 1 << " " << 0 << " ";
			if (surface[i] == "S1") { //If the surface is S1
				outfile << IEN[0][ien_py[i][j] - 1] << " ";
				outfile << IEN[1][ien_py[i][j] - 1] << " ";
				outfile << IEN[2][ien_py[i][j] - 1] << " ";
				outfile << IEN[3][ien_py[i][j] - 1] << " ";
			}
			else if (surface[i] == "S2") { //If the surface is S2 
				outfile << IEN[4][ien_py[i][j] - 1] << " ";
				outfile << IEN[5][ien_py[i][j] - 1] << " ";
				outfile << IEN[6][ien_py[i][j] - 1] << " ";
				outfile << IEN[7][ien_py[i][j] - 1] << " ";
			}
			else if (surface[i] == "S3") { //If the surface is S3
				outfile << IEN[4][ien_py[i][j] - 1] << " ";
				outfile << IEN[0][ien_py[i][j] - 1] << " ";
				outfile << IEN[1][ien_py[i][j] - 1] << " ";
				outfile << IEN[5][ien_py[i][j] - 1] << " ";
			}
			else if (surface[i] == "S4") { //If the surface is S4
				outfile << IEN[5][ien_py[i][j] - 1] << " ";
				outfile << IEN[1][ien_py[i][j] - 1] << " ";
				outfile << IEN[2][ien_py[i][j] - 1] << " ";
				outfile << IEN[6][ien_py[i][j] - 1] << " ";
			}
			else if (surface[i] == "S5") { //If the surface is S5
				outfile << IEN[7][ien_py[i][j] - 1] << " ";
				outfile << IEN[6][ien_py[i][j] - 1] << " ";
				outfile << IEN[2][ien_py[i][j] - 1] << " ";
				outfile << IEN[3][ien_py[i][j] - 1] << " ";
			}
			else if (surface[i] == "S6") { //If the surface is S6
				outfile << IEN[4][ien_py[i][j] - 1] << " ";
				outfile << IEN[7][ien_py[i][j] - 1] << " ";
				outfile << IEN[3][ien_py[i][j] - 1] << " ";
				outfile << IEN[0][ien_py[i][j] - 1] << " ";
			}
			ct += 1;
			outfile << std::endl;
		}
	}
	//write elements (the whole domain, the last physical group)
	for (int i = 0; i < NEL; i++) { //5 stands for hexahedral element
		outfile << ct << " " << 5 << " " << 2 << " " << num_sidesets + 1 << " " << 0 << " ";
		for (int j = 0; j < 8; j++) {
			outfile << IEN[j][i] << " ";
		}
		ct += 1;
		outfile << std::endl;
	}
	outfile << "$EndElements" << std::endl;
    return 0;
}