import pandas as pd 

def get_dataset():
    file_path = "e7_data/drafts_dataset.csv"
    dataset = pd.read_csv(file_path)
    return dataset

def first_picks():
    dataset = get_dataset()
        
    first_picked_col_all = []
    for index, row in dataset.iterrows():
        if row['is_first'] == 1:
            val = row['main1']
            first_picked_col_all.append(val)
        else:
            val = row['enemy1']
            first_picked_col_all.append(val)
            
    dataset['first_picked'] = first_picked_col_all
    
    recommended_fp = [] 
    for i in range(40):
        recommended_fp.append(dataset['first_picked'].value_counts().index[i])
        
    return recommended_fp


def draft_response(e1, m1, e2, m2, e3, m3,
                   e4, m4, e5, m5, mpb1, mpb2, epb1, epb2):
    
    recommended_fp = first_picks()
    dataset = get_dataset() 
    
    # list to keep track of heroes to not recommend to draft
    cannot_draft = []
    response = []
    
    copy_recommended_fp = recommended_fp

    cannot_draft.append(mpb1) 
    cannot_draft.append(mpb2)
    cannot_draft.append(epb1)
    cannot_draft.append(epb2)
    
    # Main first pick
    # "first pick" placeholder for first pick 
    if m1 == "" and e1 == "":
        
        for pick in copy_recommended_fp:
            for cannotpick in cannot_draft:
                if pick == cannotpick:
                    copy_recommended_fp.remove(pick) 
                    
        # returns the next avaliable item           
        return [copy_recommended_fp[0]]
    
    # main has fp
    if m2 == "" and m3 == "":
            
        cannot_draft.append(m1)
        cannot_draft.append(e1)
        cannot_draft.append(e2)
        
        for index, row in dataset.iterrows():
            
            # enemy fp -> main 1,2 
            # enemy 1,2,3 -> main 3,4
            # enemy 1,2,3,4,5 -> main 5
            
            # m2 m3 response into e1 e2  
                
                if row['is_first'] == 0 and row['enemy1'] == e1 and row['enemy2'] == e2:
                    
                    response1 = row['main2']
                    response2 = row['main3']
                    response.append([response1, response2])
                    responses_df = pd.DataFrame(response)
                    choices = responses_df.value_counts()[:20]
                    array = [pair for pair in choices.index] 
                    
                    flattened_list = [item for sublist in array for item in sublist]
                    data_singles = list(set(flattened_list))
                    
                    for pick in data_singles:
                        for cannotpick in cannot_draft:
                            if pick == cannotpick:
                                data_singles.remove(pick)
                                
                    return data_singles[:2]
    
    if m4 == "" and m5 == "":
            
        cannot_draft.append(m1)
        cannot_draft.append(e1)
        cannot_draft.append(e2)
        cannot_draft.append(m2)
        cannot_draft.append(m3)
        cannot_draft.append(e3)
        cannot_draft.append(e4)
        
        for index, row in dataset.iterrows():
            
            # enemy fp -> main 1,2 
            # enemy 1,2,3 -> main 3,4
            # enemy 1,2,3,4,5 -> main 5
            
            # m2 m3 response into e1 e2  
                
            if row['is_first'] == 0 and row['enemy3'] == e3 and row['enemy4'] == e4:
                
                response1 = row['main4']
                response2 = row['main5']
                response.append([response1, response2])
                responses_df = pd.DataFrame(response)
                choices = responses_df.value_counts()[:20]
                array = [pair for pair in choices.index] 
                
                flattened_list = [item for sublist in array for item in sublist]
                data_singles = list(set(flattened_list))
                
                for pick in data_singles:
                    for cannotpick in cannot_draft:
                        if pick == cannotpick:
                            data_singles.remove(pick)
                            
                return data_singles[:2]
    
    
    # enemy has fp 
    
    if m1 == "" and m2 == "":
            
        cannot_draft.append(e1) 
        
        for index, row in dataset.iterrows():
        
            # input e1
            # returns m1 m2
            if row['is_first'] == 0 and row['enemy1'] == e1:
                response1 = row['main1']
                response2 = row['main2']
                response.append([response1, response2])
                responses_df = pd.DataFrame(response)
                choices = responses_df.value_counts()[:20]
                array = [pair for pair in choices.index] 
                flattened_list = [item for sublist in array for item in sublist]
                data_singles = list(set(flattened_list))
                
                for pick in data_singles:
                    for cannotpick in cannot_draft:
                        if pick == cannotpick:
                            data_singles.remove(pick)
                            
                return data_singles[:2]
        
    if m3 == "" and m4 == "":    
            
        cannot_draft.append(e1) 
        cannot_draft.append(e2) 
        cannot_draft.append(e3)
        cannot_draft.append(m1) 
        cannot_draft.append(m2)  
        
        for index, row in dataset.iterrows():
            # input e1, e2, e3
            # returns m3 m4
            if row['is_first'] == 0 and row['enemy2'] == e2 and row['enemy3'] == e3:
                response1 = row['main3']
                response2 = row['main4']
                response.append([response1, response2])
                responses_df = pd.DataFrame(response)
                choices = responses_df.value_counts()[:20]
                array = [pair for pair in choices.index] 
                flattened_list = [item for sublist in array for item in sublist]
                data_singles = list(set(flattened_list))
                
                for pick in data_singles:
                    for cannotpick in cannot_draft:
                        # if any of the picks are in the recommended, then
                        if pick == cannotpick:
                            data_singles.remove(pick)
                            
                return data_singles[:2]
            
            
        return "invalid input"
            
    if m5 == "":    
        cannot_draft.append(e1) 
        cannot_draft.append(e2) 
        cannot_draft.append(e3)
        cannot_draft.append(e4)
        cannot_draft.append(e5)
        cannot_draft.append(m1) 
        cannot_draft.append(m2) 
        cannot_draft.append(m3) 
        cannot_draft.append(m4)
        for index, row in dataset.iterrows():       
            # input e1, e2, e3, e4, e5
            # returns m5
            if row['is_first'] == 0 and  row['enemy4'] == e4 and row['enemy5'] == e5:
                response1 = row['main5']
                response.append([response1])
                responses_df = pd.DataFrame(response)
                choices = responses_df.value_counts()[:20]
                array = [pair for pair in choices.index] 
                flattened_list = [item for sublist in array for item in sublist]
                data_singles = list(set(flattened_list))
                
                for pick in data_singles:
                    for cannotpick in cannot_draft:
                        if pick == cannotpick:
                            data_singles.remove(pick)
                            
                return data_singles[:3]            
                
    else:
        if (m2 == "" and m3 == "") or (m1 == "" and m2 == "") or (m3 == "" and m4 == ""):   
            cannot_draft.append(e1) 
            cannot_draft.append(e2) 
            cannot_draft.append(e3)
            cannot_draft.append(e4)
            cannot_draft.append(e5)
            cannot_draft.append(m1) 
            cannot_draft.append(m2) 
            cannot_draft.append(m3) 
            cannot_draft.append(m4)
            for index, row in dataset.iterrows(): 
                if row['is_first'] == 0: 
                    response1 = row['enemy3']
                    response2 = row['enemy4']
                    response.append([response1, response2])
                    responses_df = pd.DataFrame(response)
                    choices = responses_df.value_counts()[:20]
                    array = [pair for pair in choices.index] 
                    flattened_list = [item for sublist in array for item in sublist]
                    data_singles = list(set(flattened_list))
                    
                    for pick in data_singles:
                        for cannotpick in cannot_draft:
                            if pick == cannotpick:
                                data_singles.remove(pick)
                                        
                    # return data_singles[:3]
                    return "Fail 1"
                
        if m5 == "":
            cannot_draft.append(e1) 
            cannot_draft.append(e2) 
            cannot_draft.append(e3)
            cannot_draft.append(e4)
            cannot_draft.append(e5)
            cannot_draft.append(m1) 
            cannot_draft.append(m2) 
            cannot_draft.append(m3) 
            cannot_draft.append(m4)
            for index, row in dataset.iterrows(): 
                if row['is_first'] == 0: 
                    response1 = row['enemy5']
                    response.append([response1])
                    responses_df = pd.DataFrame(response)
                    choices = responses_df.value_counts()[:20]
                    array = [pair for pair in choices.index] 
                    flattened_list = [item for sublist in array for item in sublist]
                    data_singles = list(set(flattened_list))
                    
                    for pick in data_singles:
                        for cannotpick in cannot_draft:
                            if pick == cannotpick:
                                data_singles.remove(pick)
                                        
                    # return data_singles[:3]
                    return "Fail 2"
        else:                          
            return "Invalid Input"   
    