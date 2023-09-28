from config import config
import psycopg2
from Excel_Export_Templates import material_order
import pandas as pd
from datetime import *
import PyQt6.QtCore

def flow_matorder(proxy, model, numorder, numorder_pedmat, variable):
    id_list=[]
    orifice_flange_list = []
    line_flange_list = []
    gasket_list = []
    bolts_list = []
    plugs_list = []
    extractor_list = []
    plate_list = []
    nipple_list = []
    handle_list = []
    chring_list = []
    tube_list = []
    piece2_list = []

    for row in range(proxy.rowCount()):
        first_column_value = proxy.data(proxy.index(row, 0))
        id_list.append(first_column_value)

    commands_numot = ("""SELECT "ot_num"
                        FROM fabrication.fab_order
                        WHERE NOT "ot_num" LIKE '90%'
                        ORDER BY "ot_num" ASC
                        """)
    check_otpedmat = f"SELECT * FROM fabrication.fab_order WHERE id = '{numorder_pedmat + '-PEDMAT'}'"
    commands_otpedmat = ("""
                            INSERT INTO fabrication.fab_order (
                            "id","tag","element","qty_element",
                            "ot_num","qty_ot","start_date")
                            VALUES (%s,%s,%s,%s,%s,%s,%s)
                            """)
    conn = None
    try:
    # read the connection parameters
        params = config()
    # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
    # execution of commands
        cur.execute(commands_numot)
        results=cur.fetchall()
        num_ot=results[-1][0]
        cur.execute(check_otpedmat)
        results=cur.fetchall()
        if len(results) == 0:
            data=(numorder_pedmat + '-PEDMAT', numorder_pedmat, 'PEDIDO DE MATERIALES', 1, '{:06}'.format(int(num_ot) + 1), len(id_list), date.today().strftime("%d/%m/%Y"))
            cur.execute(commands_otpedmat, data)
    # close communication with the PostgreSQL database server
        cur.close()
    # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    for element in id_list:
        for row in range(model.rowCount()):
            if model.data(model.index(row, 0)) == element:
                target_row = row
                break
        if target_row is not None:
            code_orifice_flange = model.data(model.index(target_row, 69))
            codefab_orifice_flange = model.data(model.index(target_row, 70))
            code_line_flange = model.data(model.index(target_row, 72))
            codefab_line_flange = model.data(model.index(target_row, 73))
            code_gasket = model.data(model.index(target_row, 75))
            codefab_gasket = model.data(model.index(target_row, 76))
            code_bolts = model.data(model.index(target_row, 78))
            codefab_bolts = model.data(model.index(target_row, 79))
            code_plugs = model.data(model.index(target_row, 81))
            codefab_plugs = model.data(model.index(target_row, 82))
            code_extractor = model.data(model.index(target_row, 84))
            codefab_extractor = model.data(model.index(target_row, 85))
            code_plate = model.data(model.index(target_row, 87))
            codefab_plate = model.data(model.index(target_row, 88))
            code_nipple = model.data(model.index(target_row, 90))
            codefab_nipple = model.data(model.index(target_row, 91))
            code_handle = model.data(model.index(target_row, 93))
            codefab_handle = model.data(model.index(target_row, 94))
            code_chring = model.data(model.index(target_row, 96))
            codefab_chring = model.data(model.index(target_row, 97))
            code_tube = model.data(model.index(target_row, 99))
            codefab_tube = model.data(model.index(target_row, 100))
            code_piece2 = model.data(model.index(target_row, 102))
            codefab_piece2 = model.data(model.index(target_row, 103))
            all_list_parts =[]

            if code_orifice_flange != '':
                tradcodbror = ("BRIDA DE ORIFICIO " + 
                                ("WN" if model.data(model.index(target_row, 14)) == "SW/WN" else model.data(model.index(target_row, 14))) + " " + 
                                model.data(model.index(target_row, 9)) + " " + 
                                (model.data(model.index(target_row, 10)) if model.data(model.index(target_row, 10)) != "150/300" else model.data(model.index(target_row, 10))[4:4+4]) + " " + 
                                model.data(model.index(target_row, 11)))
                schbror = model.data(model.index(target_row, 12))
                designbror = model.data(model.index(target_row, 105)).replace('.',',')
                processbror = model.data(model.index(target_row, 35))
                materialbror = model.data(model.index(target_row, 13))
                qtybror = 2
                orifice_flange_list.append([code_orifice_flange,codefab_orifice_flange,tradcodbror,schbror,designbror,processbror,materialbror,qtybror])
                all_list_parts.append(orifice_flange_list)

            if code_line_flange != '':
                tradcodbrline = ("BRIDA DE LÍNEA " + 
                                ("SW" if model.data(model.index(target_row, 14)) == "SW/WN" else model.data(model.index(target_row, 14))) + " " + 
                                model.data(model.index(target_row, 9)) + " " + 
                                (model.data(model.index(target_row, 10)) if model.data(model.index(target_row, 10)) != "150/300" else model.data(model.index(target_row, 10))[0:3]) + " " + 
                                model.data(model.index(target_row, 11)))
                schbrline = model.data(model.index(target_row, 12))
                designbrline = model.data(model.index(target_row, 105)).replace('.',',')
                processbrline = model.data(model.index(target_row, 35))
                materialbrline = model.data(model.index(target_row, 13))
                qtybrline = 2
                line_flange_list.append([code_line_flange,codefab_line_flange,tradcodbrline,schbrline,designbrline,processbrline,materialbrline,qtybrline])
                all_list_parts.append(line_flange_list)

            if code_gasket != '':
                tradcodgasket = model.data(model.index(target_row, 21))
                schgasket = (model.data(model.index(target_row, 9)) + " " + 
                                model.data(model.index(target_row, 10)) + " " + 
                                model.data(model.index(target_row, 11)))
                designgasket = ''
                processgasket = ''
                materialgasket = ''
                qtygasket = 2
                gasket_list.append([code_gasket,codefab_gasket,tradcodgasket,schgasket,designgasket,processgasket,materialgasket,qtygasket])
                all_list_parts.append(gasket_list)

            if code_bolts != '':
                tradcodbolts = ('ESPÁRRAGO '+ model.data(model.index(target_row, 59)))
                modelbolts = (model.data(model.index(target_row, 9)) + " " + 
                                model.data(model.index(target_row, 10)) + " " + 
                                model.data(model.index(target_row, 11)))
                designbolts = ('esp. placa ' + model.data(model.index(target_row, 19)))
                processbolts = ''
                materialbolts = model.data(model.index(target_row, 22))
                qtybolts = model.data(model.index(target_row, 60))
                bolts_list.append([code_bolts,codefab_bolts,tradcodbolts,modelbolts,designbolts,processbolts,materialbolts,qtybolts])
                all_list_parts.append(bolts_list)

            if code_extractor != '':
                tradcodextractor = ('Extractor ' + model.data(model.index(target_row, 61)))
                sizebrida = (model.data(model.index(target_row, 9)) + " " + 
                                model.data(model.index(target_row, 10)) + " " + 
                                model.data(model.index(target_row, 11)))
                designextractor = ('esp. placa ' + model.data(model.index(target_row, 19)))
                processextractor = ''
                materialextractor = model.data(model.index(target_row, 22))[:model.data(model.index(target_row, 22)).find(' / ')]
                qtyextractor = model.data(model.index(target_row, 62))
                extractor_list.append([code_extractor,codefab_extractor,tradcodextractor,sizebrida,designextractor,processextractor,materialextractor,qtyextractor])
                all_list_parts.append(extractor_list)

            if code_plate != '':
                tradcodplate = (('ORIFICIO DE RESTRICCIÓN ' + model.data(model.index(target_row, 9)) + " " + 
                                model.data(model.index(target_row, 10)) + " " + 
                                model.data(model.index(target_row, 11))) if model.data(model.index(target_row, 18)) =='RO' else 
                                ('PLACA DE ORIFICIO ' + model.data(model.index(target_row, 9)) + " " + 
                                model.data(model.index(target_row, 10)) + " " + 
                                model.data(model.index(target_row, 11))))
                modelplate = ('ESP ' + model.data(model.index(target_row, 19)) + 'mm')
                diamextplate = model.data(model.index(target_row, 57))
                processplate = 'ARAMCO' if model.data(model.index(target_row, 20)) =='ARA' else ''
                materialplate = model.data(model.index(target_row, 17))
                qtyplate = model.data(model.index(target_row, 24)) if model.data(model.index(target_row, 8)) == "MULTISTAGE RO" else 1
                plate_list.append([code_plate,codefab_plate,tradcodplate,modelplate,diamextplate,processplate,materialplate,qtyplate])
                all_list_parts.append(plate_list)

            if code_nipple != '':
                tradcodnipple = ('NIPLO ' + model.data(model.index(target_row, 52)))
                modelnipple = ''
                designnipple = ''
                processnipple = ''
                materialnipple = model.data(model.index(target_row, 13))
                qtynipple = model.data(model.index(target_row, 53))
                nipple_list.append([code_nipple,codefab_nipple,tradcodnipple,modelnipple,designnipple,processnipple,materialnipple,qtynipple])
                all_list_parts.append(nipple_list)

            if code_handle != '':
                tradcodhandle = ('MANGO ' + model.data(model.index(target_row, 58)))
                modelhandle = (model.data(model.index(target_row, 58)) + 'mm')
                designhandle = model.data(model.index(target_row, 20))
                processhandle = ''
                materialhandle = '316SS'
                qtyhandle = 1
                handle_list.append([code_handle,codefab_handle,tradcodhandle,modelhandle,designhandle,processhandle,materialhandle,qtyhandle])
                all_list_parts.append(handle_list)

            if code_chring != '':
                tradcodchring = ('CÁMARA ANULAR ' + model.data(model.index(target_row, 9)) + " " + 
                                (model.data(model.index(target_row, 10)) if model.data(model.index(target_row, 10)) != "150/300" else model.data(model.index(target_row, 10))[0:3]) + " " + 
                                model.data(model.index(target_row, 11)))
                schchring = 'ESP ' if model.data(model.index(target_row, 11)) != "RTJ" else 'ESP 38,1MM'
                designchring = model.data(model.index(target_row, 57))
                processchring = model.data(model.index(target_row, 35))
                materialchring = model.data(model.index(target_row, 13))
                qtychring = 1
                chring_list.append([code_chring,codefab_chring,tradcodchring,schchring,designchring,processchring,materialchring,qtychring])
                all_list_parts.append(chring_list)

            if code_plugs != '':
                tradcodplug = ('TAPÓN ' + model.data(model.index(target_row, 81))[2:2 + model.data(model.index(target_row, 81)).find('-') - 4] + 'M')
                modelplug = ''
                designplug = ''
                processplug = ''
                materialplug = 'ASTM A105' if model.data(model.index(target_row, 81))[-2:] == 'C1' else model.data(model.index(target_row, 13))
                qtyplug = model.data(model.index(target_row, 51))
                plugs_list.append([code_plugs,codefab_plugs,tradcodplug,modelplug,designplug,processplug,materialplug,qtyplug])
                all_list_parts.append(plugs_list)

            if code_tube != '':
                tradcodtube = ('TUBO ' + model.data(model.index(target_row, 9)) + " sch " + model.data(model.index(target_row, 12)))
                schtube = model.data(model.index(target_row, 12))
                designtube = model.data(model.index(target_row, 105)).replace('.',',')
                processtube = ''
                commands_flangecode = ("""
                    SELECT code
                    FROM validation_data.flow_flange_material
                    WHERE flange_material = %s
                    """)
                commands_tubematerial = ("""
                    SELECT tube_material
                    FROM validation_data.flow_tube_material
                    WHERE code = %s
                    """)
                conn = None
                try:
                # read the connection parameters
                    params = config()
                # connect to the PostgreSQL server
                    conn = psycopg2.connect(**params)
                    cur = conn.cursor()
                # execution of commands one by one
                    cur.execute(commands_flangecode,(model.data(model.index(target_row, 13)),))
                    results=cur.fetchone()
                    code=results[0]
                    cur.execute(commands_tubematerial,(code,))
                    results=cur.fetchall()
                    materialtube = results[0]
                # close communication with the PostgreSQL database server
                    cur.close()
                # commit the changes
                    conn.commit()
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
                finally:
                    if conn is not None:
                        conn.close()
                qtytube = model.data(model.index(target_row, 101))
                tube_list.append([code_tube,codefab_tube,tradcodtube,schtube,designtube,processtube,materialtube,qtytube])
                all_list_parts.append(tube_list)

            if code_piece2 != '':
                tradcodpiece2 = ('CUÑA PARA WEDGE DE ' + model.data(model.index(target_row, 9)))
                commands_thk = ("""
                    SELECT wall_thk
                    FROM validation_data.pipe_diam
                    WHERE (line_size = %s
                    AND
                    sch = %s)
                    """)
                conn = None
                try:
                # read the connection parameters
                    params = config()
                # connect to the PostgreSQL server
                    conn = psycopg2.connect(**params)
                    cur = conn.cursor()
                # execution of commands one by one
                    cur.execute(commands_thk,(model.data(model.index(target_row, 9)),model.data(model.index(target_row, 12)),))
                    results=cur.fetchone()
                    thkmin=results[0]
                # close communication with the PostgreSQL database server
                    cur.close()
                # commit the changes
                    conn.commit()
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
                finally:
                    if conn is not None:
                        conn.close()
                modelpiece2 = ('Th mín ' + thkmin + 'mm')
                designpiece2 = ''
                processpiece2 = ''
                commands_flangecode = ("""
                    SELECT code
                    FROM validation_data.flow_flange_material
                    WHERE flange_material = %s
                    """)
                commands_sheetmaterial = ("""
                    SELECT sheet_material
                    FROM validation_data.flow_sheet_material
                    WHERE code = %s
                    """)
                conn = None
                try:
                # read the connection parameters
                    params = config()
                # connect to the PostgreSQL server
                    conn = psycopg2.connect(**params)
                    cur = conn.cursor()
                # execution of commands one by one
                    cur.execute(commands_flangecode,(model.data(model.index(target_row, 13)),))
                    results=cur.fetchone()
                    code=results[0]
                    cur.execute(commands_sheetmaterial,(code,))
                    results=cur.fetchall()
                    materialpiece2 = results[0]
                # close communication with the PostgreSQL database server
                    cur.close()
                # commit the changes
                    conn.commit()
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
                finally:
                    if conn is not None:
                        conn.close()
                qtypiece2 = 1
                piece2_list.append([code_piece2,codefab_piece2,tradcodpiece2,modelpiece2,designpiece2,processpiece2,materialpiece2,qtypiece2])
                all_list_parts.append(piece2_list)

            columns_equipments = ["code_equipment", "code_fab_equipment", "translate_equipment", "section_type", "f_orifice_flange",
                                    "qty_f_orifice_flange", "f_line_flange", "qty_f_line_flange", "f_gasket", "qty_f_gasket",
                                    "f_bolts", "qty_f_bolts", "f_plug", "qty_f_plug", "f_extractor",
                                    "qty_f_extractor", "f_plate", "qty_f_plate", "f_nipple", "qty_f_nipple",
                                    "f_handle", "qty_f_handle", "f_chring", "qty_f_chring", "f_tube",
                                    "qty_f_tube", "f_piece2", "qty_f_piece2"]
            columns_parts = ["code_part", "code_fab_part", "code_element", "model", "design", "process", "material", "section_type"]
            columns_tags = ["code", "equipment", "num_order","order_material","contractual_date","inspection"]
            values_equipments = [model.data(model.index(target_row, 66)), model.data(model.index(target_row, 67)), model.data(model.index(target_row, 68)), "Q-CAUD",
                                model.data(model.index(target_row, 69)), model.data(model.index(target_row, 71)), model.data(model.index(target_row, 72)), model.data(model.index(target_row, 74)),
                                model.data(model.index(target_row, 75)), model.data(model.index(target_row, 77)), model.data(model.index(target_row, 78)), model.data(model.index(target_row, 80)),
                                model.data(model.index(target_row, 81)), model.data(model.index(target_row, 83)), model.data(model.index(target_row, 84)), model.data(model.index(target_row, 86)),
                                model.data(model.index(target_row, 87)), model.data(model.index(target_row, 89)), model.data(model.index(target_row, 90)), model.data(model.index(target_row, 92)),
                                model.data(model.index(target_row, 93)), model.data(model.index(target_row, 95)), model.data(model.index(target_row, 96)), model.data(model.index(target_row, 98)),
                                model.data(model.index(target_row, 99)), model.data(model.index(target_row, 101)), model.data(model.index(target_row, 102)), model.data(model.index(target_row, 104))]
            values_tags = [model.data(model.index(target_row, 4)) + "-" + model.data(model.index(target_row, 8)) + "-" + model.data(model.index(target_row, 1)), 
                            model.data(model.index(target_row, 66)), model.data(model.index(target_row, 4)), model.data(model.index(target_row, 42)),
                            model.data(model.index(target_row, 31)), model.data(model.index(target_row, 64))]

            columns_equipments  = ", ".join([f'"{column}"' for column in columns_equipments])
            values_equipments =  ", ".join(['NULL' if value == '' or value == 0 else (str(value) if isinstance(value, (int, float)) else f"'{str(value)}'") for value in values_equipments])

            columns_tags  = ", ".join([f'"{column}"' for column in columns_tags])
            values_tags =  ", ".join(['NULL' if value == '' or value == PyQt6.QtCore.QDate() else (str(value) if isinstance(value, (int, float)) else (f"'{value.toString('yyyy-MM-dd')}'" if isinstance(value, PyQt6.QtCore.QDate) else f"'{str(value)}'")) for value in values_tags])

            columns_parts = ", ".join([f'"{column}"' for column in columns_parts])

            commands_equipments = f"INSERT INTO fabrication.equipments ({columns_equipments}) VALUES ({values_equipments})"
            commands_tags = f"INSERT INTO fabrication.tags ({columns_tags}) VALUES ({values_tags})"

            check_equipments = f"SELECT * FROM fabrication.equipments WHERE code_equipment = '{model.data(model.index(target_row, 66))}'"

            conn = None
            try:
            # read the connection parameters
                params = config()
            # connect to the PostgreSQL server
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
            # execution of commands
                cur.execute(check_equipments)
                results=cur.fetchall()
                if len(results) == 0:
                    cur.execute(commands_equipments)
                else:
                    set_clause = ", ".join([f"{column} = {value}" for column, value in zip(columns_equipments.split(", ")[1:], values_equipments.split(", ")[1:])])
                    update_equipments = f"UPDATE fabrication.equipments SET {set_clause} WHERE code_equipment = '{model.data(model.index(target_row, 66))}'"
                    cur.execute(update_equipments)

                for list_part in all_list_parts:
                    check_parts = f"SELECT * FROM fabrication.parts WHERE code_part = '{list_part[0][0]}'"
                    cur.execute(check_parts)
                    results=cur.fetchall()
                    if len(results) == 0:
                        list_part_modified = list_part[0].copy()
                        list_part_modified[-1] = 'Q-CAUD'
                        values_parts = ", ".join('NULL' if value == '' else (str(value) if isinstance(value, (int, float)) else f"'{str(value)}'") for value in list_part_modified)
                        commands_parts = f"INSERT INTO fabrication.parts ({columns_parts}) VALUES ({values_parts})"
                        cur.execute(commands_parts)
                    else:
                        list_part_modified = list_part[0].copy()
                        list_part_modified[-1] = 'Q-CAUD'
                        values_parts = ", ".join('NULL' if value == '' else (str(value) if isinstance(value, (int, float)) else f"'{str(value)}'") for value in list_part_modified)
                        set_clause = ", ".join([f"{column} = {value}" for column, value in zip(columns_parts.split(", ")[1:], values_parts.split(", ")[1:])])
                        update_parts = f"UPDATE fabrication.parts SET {set_clause} WHERE code_part = '{list_part[0][0]}'"
                        cur.execute(update_parts)

                cur.execute(commands_tags)
            # close communication with the PostgreSQL database server
                cur.close()
            # commit the changes
                conn.commit()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                if conn is not None:
                    conn.close()

# Turn all lists in dataframe and grouped in order to sum same items
    data_lists = [
    (orifice_flange_list, "df_orifice_flange"),
    (line_flange_list, "df_line_flange"),
    (gasket_list, "df_gasket"),
    (bolts_list, "df_bolts"),
    (plugs_list, "df_plugs"),
    (extractor_list, "df_extractor"),
    (plate_list, "df_plate"),
    (nipple_list, "df_nipple"),
    (handle_list, "df_handle"),
    (chring_list, "df_chring"),
    (tube_list, "df_tube"),
    (piece2_list, "df_piece2")]

    data_frames_with_data = []

    for data_list, df_name in data_lists:
        if data_list:
            sublists = [sublist[2:] for sublist in data_list]
            df = pd.DataFrame(sublists)
            df = df.groupby([0, 1, 2, 3, 4])[5].sum().reset_index()
            data_frames_with_data.append(df)

    if data_frames_with_data:
        df_combined = pd.concat(data_frames_with_data, ignore_index=True)

    commands_client = ("""
                SELECT orders."num_order",orders."num_offer",offers."client"
                FROM offers
                INNER JOIN orders ON (offers."num_offer"=orders."num_offer")
                WHERE UPPER(orders."num_order") LIKE UPPER('%%'||%s||'%%')
                """)
    conn = None
    try:
    # read the connection parameters
        params = config()
    # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
    # execution of commands one by one
        cur.execute(commands_client,(numorder,))
        results=cur.fetchone()
        client=results[2]
    # close communication with the PostgreSQL database server
        cur.close()
    # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    excel_mat_order = material_order(df_combined,numorder_pedmat,client,variable,num_ot)
    excel_mat_order.save_excel()


def temp_matorder(proxy, model, numorder, numorder_pedmat, variable):
    id_list=[]
    bar_list = []
    tube_list = []
    flange_list = []
    sensor_list = []
    head_list = []
    btb_list = []
    nipple_list = []
    spring_list = []
    plug_list = []
    puntal_list = []
    tw_list = []
    extcable_list = []

    for row in range(proxy.rowCount()):
        first_column_value = proxy.data(proxy.index(row, 0))
        id_list.append(first_column_value)

    commands_numot = ("""SELECT "ot_num"
                        FROM fabrication.fab_order
                        WHERE NOT "ot_num" LIKE '90%'
                        ORDER BY "ot_num" ASC
                        """)
    check_otpedmat = f"SELECT * FROM fabrication.fab_order WHERE id = '{numorder_pedmat + '-PEDMAT'}'"
    commands_otpedmat = ("""
                            INSERT INTO fabrication.fab_order (
                            "id","tag","element","qty_element",
                            "ot_num","qty_ot","start_date")
                            VALUES (%s,%s,%s,%s,%s,%s,%s)
                            """)
    conn = None
    try:
    # read the connection parameters
        params = config()
    # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
    # execution of commands
        cur.execute(commands_numot)
        results=cur.fetchall()
        num_ot=results[-1][0]
        cur.execute(check_otpedmat)
        results=cur.fetchall()
        if len(results) == 0:
            data=(numorder_pedmat + '-PEDMAT', numorder_pedmat, 'PEDIDO DE MATERIALES', 1, '{:06}'.format(int(num_ot) + 1), len(id_list), date.today().strftime("%d/%m/%Y"))
            cur.execute(commands_otpedmat, data)
    # close communication with the PostgreSQL database server
        cur.close()
    # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    for element in id_list:
        for row in range(model.rowCount()):
            if model.data(model.index(row, 0)) == element:
                target_row = row
                break
        if target_row is not None:
            code_bar = model.data(model.index(target_row, 76))
            codefab_bar = model.data(model.index(target_row, 77))
            code_tube = model.data(model.index(target_row, 79))
            codefab_tube = model.data(model.index(target_row, 80))
            code_flange = model.data(model.index(target_row, 82))
            codefab_flange = model.data(model.index(target_row, 83))
            code_sensor = model.data(model.index(target_row, 85))
            codefab_sensor = model.data(model.index(target_row, 86))
            code_head = model.data(model.index(target_row, 88))
            codefab_head = model.data(model.index(target_row, 89))
            code_btb = model.data(model.index(target_row, 91))
            codefab_btb = model.data(model.index(target_row, 92))
            code_nipple = model.data(model.index(target_row, 94))
            codefab_nipple = model.data(model.index(target_row, 95))
            code_spring = model.data(model.index(target_row, 97))
            codefab_spring = model.data(model.index(target_row, 98))
            code_puntal = model.data(model.index(target_row, 100))
            codefab_puntal = model.data(model.index(target_row, 101))
            code_plug = model.data(model.index(target_row, 103))
            codefab_plug = model.data(model.index(target_row, 104))
            code_tw = model.data(model.index(target_row, 106))
            codefab_tw = model.data(model.index(target_row, 107))
            code_extcable = model.data(model.index(target_row, 109))
            codefab_extcable = model.data(model.index(target_row, 110))
            all_list_parts =[]

            if code_bar != '':
                tradcodbar =('VAN STONE ' + model.data(model.index(target_row, 10)) + " " + model.data(model.index(target_row, 11)) + " " + 
                            model.data(model.index(target_row, 12)) + ' ø=' if model.data(model.index(target_row, 9)) == 'Van-Stone TW'
                            else 'BARRA VAINA PARA RAIZ ø=' + model.data(model.index(target_row, 17)))
                modelbar = ('U=' + model.data(model.index(target_row, 16)) + ' /L=' + model.data(model.index(target_row, 15)) if model.data(model.index(target_row, 9)) == 'Van-Stone TW'
                            else 'Barra ø=' + '35' if float(model.data(model.index(target_row, 17)))<=33.5 else model.data(model.index(target_row, 17)))
                notesbar = ('RAÍZ ø=' + model.data(model.index(target_row, 17)) if model.data(model.index(target_row, 9)) == 'Van-Stone TW'
                            else '')
                processbar = ''
                materialbar = model.data(model.index(target_row, 14))
                qtybar = model.data(model.index(target_row, 78))
                bar_list.append([code_bar,codefab_bar,tradcodbar,modelbar,notesbar,processbar,materialbar,qtybar])
                all_list_parts.append(bar_list)

            if code_tube != '':
                tradcodtube = 'TUBO VAINA'
                schtube = model.data(model.index(target_row, 33))
                notestube = ''
                processtube = ''
                materialtube = model.data(model.index(target_row, 14))
                qtytube = model.data(model.index(target_row, 81))
                tube_list.append([code_tube,codefab_tube,tradcodtube,schtube,notestube,processtube,materialtube,qtytube])
                all_list_parts.append(tube_list)

            if code_flange != '':
                tradcodflange = ('BRIDA VAINA ' + model.data(model.index(target_row, 10)) + model.data(model.index(target_row, 11)) + " " + 
                                model.data(model.index(target_row, 12)))
                modelflange = ''
                notesflange = ''
                processflange = ''
                materialflange = (model.data(model.index(target_row, 30)) if model.data(model.index(target_row, 9)) == 'Van-Stone TW'
                                    else model.data(model.index(target_row, 14)))
                qtyflange = 1
                flange_list.append([code_flange,codefab_flange,tradcodflange,modelflange,notesflange,processflange,materialflange,qtyflange])
                all_list_parts.append(flange_list)

            if code_sensor != '':
                tradcodsensor = (model.data(model.index(target_row, 19)) + ' Sheat/Stem ø=' + model.data(model.index(target_row, 21)) + 'mm')
                modelsensor = (model.data(model.index(target_row, 28)) + '-' + model.data(model.index(target_row, 27)) if code_sensor[:4] == 'BIME'
                                else '')
                notesensor = (model.data(model.index(target_row, 23)) + '-' + model.data(model.index(target_row, 24)) if code_sensor[:4] == 'BIME'
                                else '')
                processsensor = ''
                materialsensor = ('PT100' if tradcodsensor[:5] == 'PT100'
                                else model.data(model.index(target_row, 20)))
                qtysensor = (1 if tradcodsensor[:5] == 'PT100' or code_sensor[:4] == 'BIME'
                                else (float(model.data(model.index(target_row, 68)))/1000) if model.data(model.index(target_row, 68)) != '' else '')
                sensor_list.append([code_sensor,codefab_sensor,tradcodsensor,modelsensor,notesensor,processsensor,materialsensor,qtysensor])
                all_list_parts.append(sensor_list)

            if code_head != '':
                tradcodhead = ('CABEZA DE CONEXIONES ' + model.data(model.index(target_row, 27)))
                modelhead = model.data(model.index(target_row, 27))
                noteshead = ''
                processhead = model.data(model.index(target_row, 28))
                materialhead = ('ALUMINIO' if modelhead[-2:] == 'AL' 
                                else ('AC.CARBONO' if modelhead[-2:] == 'CS' 
                                else ('AC.INOXIDABLE' if modelhead[-2:] == 'SS' 
                                else 'MATERIAL CABEZA NO DEFINIDO')))
                qtyhead = 1
                head_list.append([code_head,codefab_head,tradcodhead,modelhead,noteshead,processhead,materialhead,qtyhead])
                all_list_parts.append(head_list)

            if code_btb != '':
                tradcodbtb = ('BIMETÁLICO-' + model.data(model.index(target_row, 28)) + '-' + model.data(model.index(target_row, 27)) if code_btb[:2] == 'BI' 
                            else ('TRANSMISOR-' + model.data(model.index(target_row, 29)) if code_btb[:2] == 'TR' 
                            else ('BLOQUE CERÁMICO-' + model.data(model.index(target_row, 29)) if code_btb[-7] == 'CE' 
                            else 'NO PREPARADO')))
                modelbtb = (model.data(model.index(target_row, 23)) + '-' + model.data(model.index(target_row, 24)) if code_btb[:2] == 'BI' 
                            else '')
                notesbtb = ''
                processbtb = ''
                materialbtb = (model.data(model.index(target_row, 20)) + '-' + model.data(model.index(target_row, 21)) if code_btb[:2] == 'BI' 
                            else ('CERÁMICO' if code_btb[:2] == 'CE' else ''))
                qtybtb = model.data(model.index(target_row, 93))
                btb_list.append([code_btb,codefab_btb,tradcodbtb,modelbtb,notesbtb,processbtb,materialbtb,qtybtb])
                all_list_parts.append(btb_list)

            if code_nipple != '':
                tradcodnipple = model.data(model.index(target_row, 25))
                modelnipple = ('' if model.data(model.index(target_row, 26)) == 'N/A' or model.data(model.index(target_row, 26))=='' else model.data(model.index(target_row, 26)))
                notesnipple = ''
                processnipple = ''
                materialnipple = tradcodnipple[tradcodnipple.find('('):tradcodnipple.find('(')+9]
                qtynipple = 1
                nipple_list.append([code_nipple,codefab_nipple,tradcodnipple,modelnipple,notesnipple,processnipple,materialnipple,qtynipple])
                all_list_parts.append(nipple_list)

            if code_spring != '':
                tradcodspring = 'MUELLE SPRING LOADER'
                modelspring = ''
                notesspring = ''
                processspring = ''
                materialspring = 'AC.INOX'
                qtyspring = 1
                spring_list.append([code_spring,codefab_spring,tradcodspring,modelspring,notesspring,processspring,materialspring,qtyspring])
                all_list_parts.append(spring_list)

            if code_plug != '':
                tradcodplug = ('TAPÓN Y CADENA-' + model.data(model.index(target_row, 69)))
                modelplug = ''
                notesplug = ''
                processplug = ''
                materialplug = tradcodplug[tradcodplug.find('('):tradcodplug.find('(')+9]
                qtyplug = 1
                plug_list.append([code_plug,codefab_plug,tradcodplug,modelplug,notesplug,processplug,materialplug,qtyplug])
                all_list_parts.append(plug_list)

            if code_puntal != '':
                tradcodpuntal = ('PUNTAL SOLDADO ' + model.data(model.index(target_row, 32)))
                modelpuntal = ''
                notespuntal = ''
                processpuntal = ''
                materialpuntal = model.data(model.index(target_row, 14))
                qtypuntal = float(code_puntal[1:8])/1000
                puntal_list.append([code_puntal,codefab_puntal,tradcodpuntal,modelpuntal,notespuntal,processpuntal,materialpuntal,qtypuntal])
                all_list_parts.append(puntal_list)

            if code_tw != '':
                tradcodtw = 'VAINA ' + model.data(model.index(target_row, 77)) + tradcodflange
                modelexttw = ''
                notesexttw = ''
                processexttw = ''
                materialexttw = ''
                qtyexttw = model.data(model.index(target_row, 108))
                tw_list.append([code_tw,codefab_tw,tradcodtw,modelexttw,notesexttw,processexttw,materialexttw,qtyexttw])
                all_list_parts.append(tw_list)

            if code_extcable != '':
                tradcodextcable = 'CABLE DE PROLONGACIÓN ' + tradcodsensor
                modelextcable = ''
                notesextcable = ''
                processextcable = ''
                materialextcable = model.data(model.index(target_row, 20))
                qtyextcable = float(model.data(model.index(target_row, 68)))/1000 if model.data(model.index(target_row, 68)) != '' else ''
                extcable_list.append([code_extcable,codefab_extcable,tradcodextcable,modelextcable,notesextcable,processextcable,materialextcable,qtyextcable])
                all_list_parts.append(extcable_list)

            columns_equipments = ["code_equipment", "code_fab_equipment", "translate_equipment", "section_type", "t_bar",
                                            "qty_t_bar", "t_tube", "qty_t_tube", "t_flange", "qty_t_flange",
                                            "t_sensor", "qty_t_sensor", "t_head", "qty_t_head", "t_btb",
                                            "qty_t_btb", "t_nippleextcomp", "qty_t_nippleextcomp", "t_spring", "qty_t_spring",
                                            "t_puntal", "qty_t_puntal", "t_plug", "qty_t_plug", "t_tw",
                                            "qty_t_tw", "t_extcable", "qty_t_extcable"]
            columns_parts = ["code_part", "code_fab_part", "code_element", "model", "design", "process", "material", "section_type"]
            columns_tags = ["code", "equipment", "num_order", "order_material", "contractual_date", "inspection"]
            values_equipments = [model.data(model.index(target_row, 73)), model.data(model.index(target_row, 74)), model.data(model.index(target_row, 75)), "T-TEMP",
                                model.data(model.index(target_row, 76)), model.data(model.index(target_row, 78)), model.data(model.index(target_row, 79)), model.data(model.index(target_row, 81)),
                                model.data(model.index(target_row, 82)), model.data(model.index(target_row, 84)), model.data(model.index(target_row, 85)), model.data(model.index(target_row, 87)),
                                model.data(model.index(target_row, 88)), model.data(model.index(target_row, 90)), model.data(model.index(target_row, 91)), model.data(model.index(target_row, 93)),
                                model.data(model.index(target_row, 94)), model.data(model.index(target_row, 96)), model.data(model.index(target_row, 97)), model.data(model.index(target_row, 99)),
                                model.data(model.index(target_row, 100)), model.data(model.index(target_row, 102)), model.data(model.index(target_row, 103)), model.data(model.index(target_row, 105)),
                                model.data(model.index(target_row, 106)), model.data(model.index(target_row, 108)), model.data(model.index(target_row, 109)), model.data(model.index(target_row, 111))]
            values_tags = [model.data(model.index(target_row, 4)) + "-" + model.data(model.index(target_row, 8)) + "-" + model.data(model.index(target_row, 1)), 
                            model.data(model.index(target_row, 73)), model.data(model.index(target_row, 4)), model.data(model.index(target_row, 62)),
                            model.data(model.index(target_row, 38)), model.data(model.index(target_row, 71))]

            columns_equipments  = ", ".join([f'"{column}"' for column in columns_equipments])
            values_equipments =  ", ".join(['NULL' if value == '' or value == 0 else (str(value) if isinstance(value, (int, float)) else f"'{str(value)}'") for value in values_equipments])

            columns_tags  = ", ".join([f'"{column}"' for column in columns_tags])
            values_tags =  ", ".join(['NULL' if value == '' or value == PyQt6.QtCore.QDate() else (str(value) if isinstance(value, (int, float)) else (f"'{value.toString('yyyy-MM-dd')}'" if isinstance(value, PyQt6.QtCore.QDate) else f"'{str(value)}'")) for value in values_tags])

            columns_parts = ", ".join([f'"{column}"' for column in columns_parts])

            commands_equipments = f"INSERT INTO fabrication.equipments ({columns_equipments}) VALUES ({values_equipments})"
            commands_tags = f"INSERT INTO fabrication.tags ({columns_tags}) VALUES ({values_tags})"

            check_equipments = f"SELECT * FROM fabrication.equipments WHERE code_equipment = '{model.data(model.index(target_row, 73))}'"

            conn = None
            try:
            # read the connection parameters
                params = config()
            # connect to the PostgreSQL server
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
            # execution of commands
                cur.execute(check_equipments)
                results=cur.fetchall()
                if len(results) == 0:
                    cur.execute(commands_equipments)
                else:
                    set_clause = ", ".join([f"{column} = {value}" for column, value in zip(columns_equipments.split(", ")[1:], values_equipments.split(", ")[1:])])
                    update_equipments = f"UPDATE fabrication.equipments SET {set_clause} WHERE code_equipment = '{model.data(model.index(target_row, 73))}'"
                    cur.execute(update_equipments)

                for list_part in all_list_parts:
                    check_parts = f"SELECT * FROM fabrication.parts WHERE code_part = '{list_part[0][0]}'"
                    cur.execute(check_parts)
                    results=cur.fetchall()
                    if len(results) == 0:
                        list_part_modified = list_part[0].copy()
                        list_part_modified[-1] = 'T-TEMP'
                        values_parts = ", ".join('NULL' if value == '' else (str(value) if isinstance(value, (int, float)) else f"'{str(value)}'") for value in list_part_modified)
                        commands_parts = f"INSERT INTO fabrication.parts ({columns_parts}) VALUES ({values_parts})"
                        cur.execute(commands_parts)
                    else:
                        list_part_modified = list_part[0].copy()
                        list_part_modified[-1] = 'T-TEMP'
                        values_parts = ", ".join('NULL' if value == '' else (str(value) if isinstance(value, (int, float)) else f"'{str(value)}'") for value in list_part_modified)
                        set_clause = ", ".join([f"{column} = {value}" for column, value in zip(columns_parts.split(", ")[1:], values_parts.split(", ")[1:])])
                        update_parts = f"UPDATE fabrication.parts SET {set_clause} WHERE code_part = '{list_part[0][0]}'"
                        cur.execute(update_parts)

                cur.execute(commands_tags)
            # close communication with the PostgreSQL database server
                cur.close()
            # commit the changes
                conn.commit()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                if conn is not None:
                    conn.close()

# Turn all lists in dataframe and grouped in order to sum same items
    data_lists = [
    (bar_list, "df_bar"),
    (tube_list, "df_tube"),
    (flange_list, "df_flange"),
    (sensor_list, "df_sensor"),
    (head_list, "df_head"),
    (btb_list, "df_btb"),
    (nipple_list, "df_nipple"),
    (spring_list, "df_spring"),
    (plug_list, "df_plug"),
    (puntal_list, "df_puntal"),
    (extcable_list, "df_extcable")]

    data_frames_with_data = []

    for data_list, df_name in data_lists:
        if data_list:
            sublists = [sublist[2:] for sublist in data_list]
            df = pd.DataFrame(sublists)
            df = df.groupby([0, 1, 2, 3, 4])[5].sum().reset_index()
            data_frames_with_data.append(df)

    if data_frames_with_data:
        df_combined = pd.concat(data_frames_with_data, ignore_index=True)

    commands_client = ("""
                        SELECT orders."num_order",orders."num_offer",offers."client"
                        FROM offers
                        INNER JOIN orders ON (offers."num_offer"=orders."num_offer")
                        WHERE UPPER(orders."num_order") LIKE UPPER('%%'||%s||'%%')
                        """)
    conn = None
    try:
    # read the connection parameters
        params = config()
    # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
    # execution of commands one by one
        cur.execute(commands_client,(numorder,))
        results=cur.fetchone()
        client=results[2]
    # close communication with the PostgreSQL database server
        cur.close()
    # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    excel_mat_order = material_order(df_combined,numorder_pedmat,client,variable,num_ot)
    excel_mat_order.save_excel()


def level_matorder(proxy, model, numorder, numorder_pedmat, variable):
    id_list = []
    body_list = []
    cover_list = []
    glass_list = []
    gasket_list = []
    mica_list = []
    bolts_list = []
    nipplehex_list = []
    valve_list = []
    flangevalve_list = []
    nippletube_list = []
    dv_list = []
    plug_list = []
    antifrost_list = []
    illuminator_list = []

    for row in range(proxy.rowCount()):
        first_column_value = proxy.data(proxy.index(row, 0))
        id_list.append(first_column_value)

    commands_numot = ("""SELECT "ot_num"
                        FROM fabrication.fab_order
                        WHERE NOT "ot_num" LIKE '90%'
                        ORDER BY "ot_num" ASC
                        """)
    check_otpedmat = f"SELECT * FROM fabrication.fab_order WHERE id = '{numorder_pedmat + '-PEDMAT'}'"
    commands_otpedmat = ("""
                            INSERT INTO fabrication.fab_order (
                            "id","tag","element","qty_element",
                            "ot_num","qty_ot","start_date")
                            VALUES (%s,%s,%s,%s,%s,%s,%s)
                            """)
    conn = None
    try:
    # read the connection parameters
        params = config()
    # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
    # execution of commands
        cur.execute(commands_numot)
        results=cur.fetchall()
        num_ot=results[-1][0]
        cur.execute(check_otpedmat)
        results=cur.fetchall()
        if len(results) == 0:
            data=(numorder_pedmat + '-PEDMAT', numorder_pedmat, 'PEDIDO DE MATERIALES', 1, '{:06}'.format(int(num_ot) + 1), len(id_list), date.today().strftime("%d/%m/%Y"))
            cur.execute(commands_otpedmat, data)
    # close communication with the PostgreSQL database server
        cur.close()
    # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    for element in id_list:
        for row in range(model.rowCount()):
            if model.data(model.index(row, 0)) == element:
                target_row = row
                break
        if target_row is not None:
            code_body = model.data(model.index(target_row, 57))
            codefab_body = model.data(model.index(target_row, 58))
            code_cover = model.data(model.index(target_row, 60))
            codefab_cover = model.data(model.index(target_row, 61))
            code_glass = model.data(model.index(target_row, 87))
            codefab_glass = model.data(model.index(target_row, 88))
            code_gasket = model.data(model.index(target_row, 84))
            codefab_gasket = model.data(model.index(target_row, 85))
            code_mica = model.data(model.index(target_row, 93))
            codefab_mica = model.data(model.index(target_row, 94))
            code_bolts = model.data(model.index(target_row, 63))
            codefab_bolts = model.data(model.index(target_row, 64))
            code_nipplehex = model.data(model.index(target_row, 66))
            codefab_nipplehex = model.data(model.index(target_row, 67))
            code_valve = model.data(model.index(target_row, 69))
            codefab_valve = model.data(model.index(target_row, 70))
            code_flangevalve = model.data(model.index(target_row, 72))
            codefab_flangevalve = model.data(model.index(target_row, 73))
            code_nippletube = model.data(model.index(target_row, 102))
            codefab_nippletube = model.data(model.index(target_row, 103))
            code_dv = model.data(model.index(target_row, 75))
            codefab_dv = model.data(model.index(target_row, 76))
            code_antifrost = model.data(model.index(target_row, 105))
            codefab_antifrost = model.data(model.index(target_row, 106))
            code_illuminator = model.data(model.index(target_row, 81))
            codefab_illuminator = model.data(model.index(target_row, 82))
            all_list_parts = []

            model_num = model.data(model.index(target_row, 9))[:6]
            conn_type = model.data(model.index(target_row, 15))
            nipplehexdim = model.data(model.index(target_row, 32))[8:]
            nippletubedim = model.data(model.index(target_row, 33))[8:]
            cc_length = int(model.data(model.index(target_row, 17)))

            commands_topbottom = ("""
                    SELECT *
                    FROM validation_data.level_topbottom_dim
                    WHERE model_num = %s
                    """)
            commands_sideside = ("""
                    SELECT *
                    FROM validation_data.level_sideside_dim
                    WHERE model_num = %s
                    """)
            conn = None
            try:
            # read the connection parameters
                params = config()
            # connect to the PostgreSQL server
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
            # execution of commands one by one
                if conn_type == 'Top-Bottom':
                    cur.execute(commands_topbottom,(model_num,))
                    results=cur.fetchone()
                    if nipplehexdim == '1/2" NPT':
                        body_length=results[1]
                    else:
                        body_length=results[2]
                elif conn_type == 'Side-Side':
                    cur.execute(commands_sideside,(model_num,))
                    results=cur.fetchone()
                    h_dim=int(results[1])
                    if cc_length < h_dim + 32:
                        body_length = cc_length + 32 + 100
                    else:
                        body_length = cc_length - 32 + 100
            # close communication with the PostgreSQL database server
                cur.close()
            # commit the changes
                conn.commit()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                if conn is not None:
                    conn.close()

            if code_body != '':
                tradcodbody = ('CUERPO DE NIVEL 1S-' + code_body + ' LONGITUD ' + str(body_length) + 'MM')
                modelbody = nipplehexdim
                designbody = '40x40'
                processbody = (nipplehexdim + '-M')
                materialbody = model.data(model.index(target_row, 10))
                qtybody = model.data(model.index(target_row, 59))
                body_list.append([code_body,codefab_body,tradcodbody,modelbody,designbody,processbody,materialbody,qtybody])
                all_list_parts.append(body_list)

            if code_cover != '':
                commands_coverdim = ("""
                    SELECT *
                    FROM validation_data.level_cover_dim
                    WHERE cover = %s
                    """)
                conn = None
                try:
                # read the connection parameters
                    params = config()
                # connect to the PostgreSQL server
                    conn = psycopg2.connect(**params)
                    cur = conn.cursor()
                # execution of commands one by one
                    cover_num = model_num[2:6]
                    cover_num = cover_num[:2] + '1' + cover_num[3:]
                    cur.execute(commands_coverdim,(cover_num,))
                    results=cur.fetchone()
                    length=results[1]
                    bores=results[2]
                # close communication with the PostgreSQL database server
                    cur.close()
                # commit the changes
                    conn.commit()
                except (Exception, psycopg2.DatabaseError) as error:
                    print(error)
                finally:
                    if conn is not None:
                        conn.close()

                tradcodcover = ('CUBIERTA DE NIVEL MODELO 1S-' + model_num[5:6])
                modelcover = ('L=' + str(length))
                designcover = '80x30'
                processcover = (str(bores) + ' taladros')
                materialcover = model.data(model.index(target_row, 10))
                qtycover = model.data(model.index(target_row, 62))
                cover_list.append([code_cover,codefab_cover,tradcodcover,modelcover,designcover,processcover,materialcover,qtycover])
                all_list_parts.append(cover_list)

            if code_glass != '':
                tradcodglass = ('VIDRIO DE NIVEL MODELO 1S-' + model_num[5:6])
                modelglass = 'TRANSPARENCIA' if model_num[6:7] == 'T' else 'REFLEXIÓN'
                designglass = ''
                processglass = ''
                materialglass ='BOROSILICATO'
                qtyglass = model.data(model.index(target_row, 89))
                glass_list.append([code_glass,codefab_glass,tradcodglass,modelglass,designglass,processglass,materialglass,qtyglass])
                all_list_parts.append(glass_list)

            if code_gasket != '':
                tradcodgasket = ('JUNTAS NORMALES MODELO 1S-' + model_num[5:6])
                modelgasket = 'TRANSPARENCIA' if model_num[6:7] == 'T' else 'REFLEXIÓN'
                designgasket = ''
                processgasket = ''
                materialgasket ='GRAFOIL'
                qtygasket = model.data(model.index(target_row, 86))
                gasket_list.append([code_gasket,codefab_gasket,tradcodgasket,modelgasket,designgasket,processgasket,materialgasket,qtygasket])
                all_list_parts.append(gasket_list)

            if code_mica != '':
                tradcodmica = ('JUNTAS NORMALES MODELO 1S-' + model_num[5:6])
                modelmica = 'TRANSPARENCIA'
                designmica = ''
                processmica = ''
                materialmica ='MICA'
                qtymica = model.data(model.index(target_row, 95))
                mica_list.append([code_mica,codefab_mica,tradcodmica,modelmica,designmica,processmica,materialmica,qtymica])
                all_list_parts.append(mica_list)

            if code_bolts != '':
                tradcodbolts = 'TIRANTE RECTO M10 (CON UNA TUERCA M10)' if model_num[6:7] == 'T' else 'ESPÁRRAGO EN "U" M10 (CON DOS TUERCAS M10)'
                modelbolts = 'TRANSPARENCIA' if model_num[6:7] == 'T' else 'REFLEXIÓN'
                designbolts = 'M10x132 mm' if model_num[6:7] == 'T' else ''
                processbolts = 'cabeza exag 17 e/c' if model_num[6:7] == 'T' else ''
                materialbolts = 'B7/2H' if model_num[6:7] in ['T','R'] else model.data(model.index(target_row, 24))
                qtybolts = model.data(model.index(target_row, 65))
                bolts_list.append([code_bolts,codefab_bolts,tradcodbolts,modelbolts,designbolts,processbolts,materialbolts,qtybolts])
                all_list_parts.append(bolts_list)

            if code_nipplehex != '':
                tradcodnipplehex = 'NIPLO HEXAGONAL ' + nipplehexdim + 'LONG ' + str(cc_length-length-72+20) + ' mm'
                modelnipplehex = (str(cc_length-length-72+20) + ' mm')
                designnipplehex = ''
                processnipplehex = ''
                materialnipplehex = model.data(model.index(target_row, 10))
                qtynipplehex = model.data(model.index(target_row, 68))
                nipplehex_list.append([code_nipplehex,codefab_nipplehex,tradcodnipplehex,modelnipplehex,designnipplehex,processnipplehex,materialnipplehex,qtynipplehex])
                all_list_parts.append(nipplehex_list)

            if code_valve != '':
                tradcodvalve = 'VÁLVULA DE NIVEL DESPLAZADO ' + model.data(model.index(target_row, 18))
                modelvalve = nipplehexdim[:4] + ' x ' + nipplehexdim[:4]
                designvalve = nipplehexdim[-3:] + '-H'
                processvalve = ''
                materialvalve = 'A-105' if model.data(model.index(target_row, 18))[-2:] == 'NB' else '316 SS'
                qtyvalve = model.data(model.index(target_row, 71))
                valve_list.append([code_valve,codefab_valve,tradcodvalve,modelvalve,designvalve,processvalve,materialvalve,qtyvalve])
                all_list_parts.append(valve_list)

            if code_flangevalve != '':
                tradcodflangevalve = 'BRIDA VÁLVULA ' + model.data(model.index(target_row, 12)) + ' ' + model.data(model.index(target_row, 13)) + ' ' + model.data(model.index(target_row, 14))
                modelflangevalve = ''
                designflangevalve = ''
                processflangevalve = ''
                materialflangevalve = model.data(model.index(target_row, 10))
                qtyflangevalve = model.data(model.index(target_row, 74))
                flangevalve_list.append([code_flangevalve,codefab_flangevalve,tradcodflangevalve,modelflangevalve,designflangevalve,processflangevalve,materialflangevalve,qtyflangevalve])
                all_list_parts.append(flangevalve_list)

            if code_dv != '':
                tradcoddv = ('TAPÓN PURGADOR ' + model.data(model.index(target_row, 20)) + model.data(model.index(target_row, 21)) if code_dv[:2] == 'PL' 
                            else ('VÁLVULA TMGV ' + nipplehexdim + ' x ' + model.data(model.index(target_row, 20)) + model.data(model.index(target_row, 21)) if code_dv[:2] == 'VL'
                            else ('BRIDA ' + model.data(model.index(target_row, 20)) + model.data(model.index(target_row, 21)) + model.data(model.index(target_row, 22)) if code_dv[:2] == 'FL' else '')))
                modeldv = ''
                designdv = ''
                processdv = ''
                materialdv = model.data(model.index(target_row, 10))
                qtydv = model.data(model.index(target_row, 77))
                dv_list.append([code_dv,codefab_dv,tradcoddv,modeldv,designdv,processdv,materialdv,qtydv])
                all_list_parts.append(dv_list)

            if tradcoddv[:3] == 'VÁL':
                tradcodplug = 'TAPÓN NORMAL ' + model.data(model.index(target_row, 20)) + model.data(model.index(target_row, 21))
                modelplug = ''
                designplug = ''
                processplug = ''
                materialplug = model.data(model.index(target_row, 10))
                qtyplug = 2
                plug_list.append([tradcodplug,modelplug,designplug,processplug,materialplug,qtyplug])

            if code_nippletube != '':
                tradcodnippletube = 'NIPLO TUBO ' + nippletubedim
                modelnippletube = '80 mm'
                designnippletube = ''
                processnippletube = ''
                materialnippletube = 'A-106' if model.data(model.index(target_row, 10)) in ['Carbon Steel','ASTM A350 LF2 CL2'] else model.data(model.index(target_row, 10))
                qtynippletube = model.data(model.index(target_row, 104))
                nippletube_list.append([code_nippletube,codefab_nippletube,tradcodnippletube,modelnippletube,designnippletube,processnippletube,materialnippletube,qtynippletube])
                all_list_parts.append(nippletube_list)

            if code_illuminator != '':
                tradcodilluminator = 'ILUMINADOR ' + model_num[3:7]
                modelilluminator = model_num[:6].replace('S','I')
                designilluminator = ''
                processilluminator = ''
                materialilluminator = 'HIERRO'
                qtyilluminator = model.data(model.index(target_row, 74))
                illuminator_list.append([code_illuminator,codefab_illuminator,tradcodilluminator,modelilluminator,designilluminator,processilluminator,materialilluminator,qtyilluminator])
                all_list_parts.append(illuminator_list)

            if code_antifrost != '':
                tradcodantifrost = 'ANTIHIELO TAMAÑO ' + model_num[3:7]
                modelantifrost = ''
                designantifrost = ''
                processantifrost = ''
                materialantifrost = 'METACRILATO'
                qtyantifrost = model.data(model.index(target_row, 107))
                antifrost_list.append([code_antifrost,codefab_antifrost,tradcodantifrost,modelantifrost,designantifrost,processantifrost,materialantifrost,qtyantifrost])
                all_list_parts.append(antifrost_list)

            columns_equipments = ["code_equipment", "code_fab_equipment", "translate_equipment", "section_type", "l_body",
                                            "qty_l_body", "l_cover", "qty_l_cover", "l_studs", "qty_l_studs",
                                            "l_nipplehex", "qty_l_nipplehex", "l_valve", "qty_l_valve", "l_flange",
                                            "qty_l_flange", "l_dv", "qty_l_dv", "l_scale", "qty_l_scale",
                                            "l_illuminator", "qty_l_illuminator", "l_gasketglass", "qty_l_gasketglass", "l_glass",
                                            "qty_l_glass", "l_float", "qty_l_float", "l_mica", "qty_l_mica",
                                            "l_flags", "qty_l_flags", "l_gasketflange", "qty_l_gasketflange", "l_nippletub",
                                            "qty_l_nippletub", "l_antifrost", "qty_l_antifrost"]
            columns_parts = ["code_part", "code_fab_part", "code_element", "model", "design", "process", "material", "section_type"]
            columns_tags = ["code", "equipment", "num_order","order_material","contractual_date","inspection"]
            values_equipments = [model.data(model.index(target_row, 54)), model.data(model.index(target_row, 55)), model.data(model.index(target_row, 56)), "N-Niveles",
                                model.data(model.index(target_row, 57)), model.data(model.index(target_row, 59)), model.data(model.index(target_row, 60)), model.data(model.index(target_row, 62)),
                                model.data(model.index(target_row, 63)), model.data(model.index(target_row, 65)), model.data(model.index(target_row, 66)), model.data(model.index(target_row, 68)),
                                model.data(model.index(target_row, 69)), model.data(model.index(target_row, 71)), model.data(model.index(target_row, 72)), model.data(model.index(target_row, 74)),
                                model.data(model.index(target_row, 75)), model.data(model.index(target_row, 77)), model.data(model.index(target_row, 78)), model.data(model.index(target_row, 80)),
                                model.data(model.index(target_row, 81)), model.data(model.index(target_row, 83)), model.data(model.index(target_row, 84)), model.data(model.index(target_row, 86)),
                                model.data(model.index(target_row, 87)), model.data(model.index(target_row, 89)), model.data(model.index(target_row, 90)), model.data(model.index(target_row, 92)),
                                model.data(model.index(target_row, 93)), model.data(model.index(target_row, 95)), model.data(model.index(target_row, 96)), model.data(model.index(target_row, 98)),
                                model.data(model.index(target_row, 99)), model.data(model.index(target_row, 101)), model.data(model.index(target_row, 102)), model.data(model.index(target_row, 104)),
                                model.data(model.index(target_row, 105)), model.data(model.index(target_row, 107))]
            values_tags = [model.data(model.index(target_row, 4)) + "-" + model.data(model.index(target_row, 8)) + "-" + model.data(model.index(target_row, 1)), 
                            model.data(model.index(target_row, 54)), model.data(model.index(target_row, 4)), model.data(model.index(target_row, 48)),
                            model.data(model.index(target_row, 39)), model.data(model.index(target_row, 52))]

            columns_equipments  = ", ".join([f'"{column}"' for column in columns_equipments])
            values_equipments =  ", ".join(['NULL' if value == '' or value == 0 else (str(value) if isinstance(value, (int, float)) else f"'{str(value)}'") for value in values_equipments])

            columns_tags  = ", ".join([f'"{column}"' for column in columns_tags])
            values_tags =  ", ".join(['NULL' if value == '' or value == PyQt6.QtCore.QDate() else (str(value) if isinstance(value, (int, float)) else (f"'{value.toString('yyyy-MM-dd')}'" if isinstance(value, PyQt6.QtCore.QDate) else f"'{str(value)}'")) for value in values_tags])

            columns_parts = ", ".join([f'"{column}"' for column in columns_parts])

            commands_equipments = f"INSERT INTO fabrication.equipments ({columns_equipments}) VALUES ({values_equipments})"
            commands_tags = f"INSERT INTO fabrication.tags ({columns_tags}) VALUES ({values_tags})"

            check_equipments = f"SELECT * FROM fabrication.equipments WHERE code_equipment = '{model.data(model.index(target_row, 54))}'"

            conn = None
            try:
            # read the connection parameters
                params = config()
            # connect to the PostgreSQL server
                conn = psycopg2.connect(**params)
                cur = conn.cursor()
            # execution of commands
                cur.execute(check_equipments)
                results=cur.fetchall()
                if len(results) == 0:
                    cur.execute(commands_equipments)
                else:
                    set_clause = ", ".join([f"{column} = {value}" for column, value in zip(columns_equipments.split(", ")[1:], values_equipments.split(", ")[1:])])
                    update_equipments = f"UPDATE fabrication.equipments SET {set_clause} WHERE code_equipment = '{model.data(model.index(target_row, 54))}'"
                    cur.execute(update_equipments)

                for list_part in all_list_parts:
                    check_parts = f"SELECT * FROM fabrication.parts WHERE code_part = '{list_part[0][0]}'"
                    cur.execute(check_parts)
                    results=cur.fetchall()
                    if len(results) == 0:
                        list_part_modified = list_part[0].copy()
                        list_part_modified[-1] = 'N-Niveles'
                        values_parts = ", ".join('NULL' if value == '' else (str(value) if isinstance(value, (int, float)) else f"'{str(value)}'") for value in list_part_modified)
                        commands_parts = f"INSERT INTO fabrication.parts ({columns_parts}) VALUES ({values_parts})"
                        cur.execute(commands_parts)
                    else:
                        list_part_modified = list_part[0].copy()
                        list_part_modified[-1] = 'N-Niveles'
                        values_parts = ", ".join('NULL' if value == '' else (str(value) if isinstance(value, (int, float)) else f"'{str(value)}'") for value in list_part_modified)
                        set_clause = ", ".join([f"{column} = {value}" for column, value in zip(columns_parts.split(", ")[1:], values_parts.split(", ")[1:])])
                        update_parts = f"UPDATE fabrication.parts SET {set_clause} WHERE code_part = '{list_part[0][0]}'"
                        cur.execute(update_parts)

                cur.execute(commands_tags)
            # close communication with the PostgreSQL database server
                cur.close()
            # commit the changes
                conn.commit()
            except (Exception, psycopg2.DatabaseError) as error:
                print(error)
            finally:
                if conn is not None:
                    conn.close()

# Turn all lists in dataframe and grouped in order to sum same items
    data_lists = [
    (body_list, "df_body"),
    (cover_list, "df_cover"),
    (glass_list, "df_glass"),
    (gasket_list, "df_gasket"),
    (mica_list, "df_mica"),
    (bolts_list, "df_bolts"),
    (nipplehex_list, "df_nipplehex"),
    (valve_list, "df_valve"),
    (flangevalve_list, "df_flangevalve"),
    (nippletube_list, "df_nippletube"),
    (dv_list, "df_list"),
    (antifrost_list, "df_antifrost"),
    (illuminator_list, "df_illuminator")]

    data_frames_with_data = []

    for data_list, df_name in data_lists:
        if data_list:
            sublists = [sublist[2:] for sublist in data_list]
            df = pd.DataFrame(sublists)
            df = df.groupby([0, 1, 2, 3, 4])[5].sum().reset_index()
            data_frames_with_data.append(df)

    if data_frames_with_data:
        df_combined = pd.concat(data_frames_with_data, ignore_index=True)

    commands_client = ("""
                        SELECT orders."num_order",orders."num_offer",offers."client"
                        FROM offers
                        INNER JOIN orders ON (offers."num_offer"=orders."num_offer")
                        WHERE UPPER(orders."num_order") LIKE UPPER('%%'||%s||'%%')
                        """)
    conn = None
    try:
    # read the connection parameters
        params = config()
    # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
    # execution of commands one by one
        cur.execute(commands_client,(numorder,))
        results=cur.fetchone()
        client=results[2]
    # close communication with the PostgreSQL database server
        cur.close()
    # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    excel_mat_order = material_order(df_combined,numorder_pedmat,client,variable,num_ot)
    excel_mat_order.save_excel()