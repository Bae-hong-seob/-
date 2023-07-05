def rotation_matrix(original):
            result = [[row[i] for row in original[::-1]] for i in range(len(original[0]))]
            
            return result

