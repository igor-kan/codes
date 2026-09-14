; ModuleID = 'algorithms/02_c/strings/manacher.c'
source_filename = "algorithms/02_c/strings/manacher.c"
target datalayout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-i128:128-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

@t = internal unnamed_addr global [200003 x i8] zeroinitializer, align 16
@p = internal unnamed_addr global [200003 x i32] zeroinitializer, align 16
@.str = private unnamed_addr constant [6 x i8] c"babad\00", align 1
@.str.2 = private unnamed_addr constant [5 x i8] c"cbbd\00", align 1
@.str.4 = private unnamed_addr constant [8 x i8] c"racecar\00", align 1
@str = private unnamed_addr constant [52 x i8] c"[C Manacher] Longest palindromic substring verified\00", align 1
@str.7 = private unnamed_addr constant [34 x i8] c"[C Manacher] FAILED: racecar -> 7\00", align 1
@str.8 = private unnamed_addr constant [31 x i8] c"[C Manacher] FAILED: cbbd -> 2\00", align 1
@str.9 = private unnamed_addr constant [32 x i8] c"[C Manacher] FAILED: babad -> 3\00", align 1

; Function Attrs: nofree norecurse nounwind sspstrong memory(readwrite, argmem: read, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable
define dso_local range(i32 0, -2147483648) i32 @manacher(ptr noundef readonly captures(none) %0) local_unnamed_addr #0 {
  %2 = tail call i64 @strlen(ptr noundef nonnull dereferenceable(1) %0) #5
  %3 = trunc i64 %2 to i32
  store i8 35, ptr @t, align 16, !tbaa !9
  %4 = icmp sgt i32 %3, 0
  br i1 %4, label %5, label %35

5:                                                ; preds = %1
  %6 = and i64 %2, 2147483647
  %7 = icmp samesign ult i64 %6, 16
  br i1 %7, label %29, label %8

8:                                                ; preds = %5
  %9 = and i64 %2, 2147483632
  %10 = shl nuw nsw i64 %9, 1
  %11 = or disjoint i64 %10, 1
  br label %12

12:                                               ; preds = %12, %8
  %13 = phi i64 [ 0, %8 ], [ %25, %12 ]
  %14 = shl i64 %13, 1
  %15 = getelementptr inbounds nuw i8, ptr %0, i64 %13
  %16 = getelementptr inbounds nuw i8, ptr %15, i64 8
  %17 = load <8 x i8>, ptr %15, align 1, !tbaa !9
  %18 = load <8 x i8>, ptr %16, align 1, !tbaa !9
  %19 = getelementptr inbounds nuw i8, ptr @t, i64 %14
  %20 = getelementptr inbounds nuw i8, ptr %19, i64 1
  %21 = getelementptr inbounds nuw i8, ptr @t, i64 %14
  %22 = getelementptr inbounds nuw i8, ptr %21, i64 17
  %23 = shufflevector <8 x i8> %17, <8 x i8> splat (i8 35), <16 x i32> <i32 0, i32 8, i32 1, i32 9, i32 2, i32 10, i32 3, i32 11, i32 4, i32 12, i32 5, i32 13, i32 6, i32 14, i32 7, i32 15>
  store <16 x i8> %23, ptr %20, align 1, !tbaa !9
  %24 = shufflevector <8 x i8> %18, <8 x i8> splat (i8 35), <16 x i32> <i32 0, i32 8, i32 1, i32 9, i32 2, i32 10, i32 3, i32 11, i32 4, i32 12, i32 5, i32 13, i32 6, i32 14, i32 7, i32 15>
  store <16 x i8> %24, ptr %22, align 1, !tbaa !9
  %25 = add nuw i64 %13, 16
  %26 = icmp eq i64 %25, %9
  br i1 %26, label %27, label %12, !llvm.loop !10

27:                                               ; preds = %12
  %28 = icmp eq i64 %6, %9
  br i1 %28, label %32, label %29

29:                                               ; preds = %5, %27
  %30 = phi i64 [ 0, %5 ], [ %9, %27 ]
  %31 = phi i64 [ 1, %5 ], [ %11, %27 ]
  br label %41

32:                                               ; preds = %41, %27
  %33 = phi i64 [ %11, %27 ], [ %47, %41 ]
  %34 = trunc nuw i64 %33 to i32
  br label %35

35:                                               ; preds = %32, %1
  %36 = phi i32 [ 1, %1 ], [ %34, %32 ]
  %37 = zext i32 %36 to i64
  %38 = getelementptr inbounds nuw i8, ptr @t, i64 %37
  store i8 0, ptr %38, align 1, !tbaa !9
  %39 = sext i32 %36 to i64
  %40 = add i32 %36, -1
  br label %52

41:                                               ; preds = %29, %41
  %42 = phi i64 [ %49, %41 ], [ %30, %29 ]
  %43 = phi i64 [ %47, %41 ], [ %31, %29 ]
  %44 = getelementptr inbounds nuw i8, ptr %0, i64 %42
  %45 = load i8, ptr %44, align 1, !tbaa !9
  %46 = getelementptr inbounds nuw i8, ptr @t, i64 %43
  store i8 %45, ptr %46, align 1, !tbaa !9
  %47 = add nuw nsw i64 %43, 2
  %48 = getelementptr inbounds nuw i8, ptr %46, i64 1
  store i8 35, ptr %48, align 1, !tbaa !9
  %49 = add nuw nsw i64 %42, 1
  %50 = icmp eq i64 %49, %6
  br i1 %50, label %32, label %41, !llvm.loop !14

51:                                               ; preds = %110
  ret i32 %116

52:                                               ; preds = %35, %110
  %53 = phi i64 [ 0, %35 ], [ %117, %110 ]
  %54 = phi i32 [ %40, %35 ], [ %118, %110 ]
  %55 = phi i32 [ 0, %35 ], [ %116, %110 ]
  %56 = phi i32 [ 0, %35 ], [ %115, %110 ]
  %57 = phi i32 [ 0, %35 ], [ %114, %110 ]
  %58 = zext nneg i32 %56 to i64
  %59 = icmp samesign ult i64 %53, %58
  br i1 %59, label %62, label %60

60:                                               ; preds = %52
  %61 = trunc nuw nsw i64 %53 to i32
  br label %71

62:                                               ; preds = %52
  %63 = shl nuw nsw i32 %57, 1
  %64 = zext nneg i32 %63 to i64
  %65 = sub nsw i64 %64, %53
  %66 = trunc nuw nsw i64 %53 to i32
  %67 = sub nsw i32 %56, %66
  %68 = getelementptr inbounds i32, ptr @p, i64 %65
  %69 = load i32, ptr %68, align 4, !tbaa !5
  %70 = tail call i32 @llvm.smin.i32(i32 %67, i32 %69)
  br label %71

71:                                               ; preds = %60, %62
  %72 = phi i32 [ %61, %60 ], [ %66, %62 ]
  %73 = phi i32 [ 0, %60 ], [ %70, %62 ]
  %74 = getelementptr inbounds nuw i32, ptr @p, i64 %53
  %75 = add nsw i32 %73, %72
  %76 = add nsw i32 %75, 1
  %77 = icmp slt i32 %76, %36
  br i1 %77, label %78, label %110

78:                                               ; preds = %71
  %79 = xor i32 %73, -1
  %80 = add i32 %72, %79
  %81 = icmp sgt i32 %80, -1
  br i1 %81, label %82, label %110

82:                                               ; preds = %78
  %83 = sext i32 %73 to i64
  br label %91

84:                                               ; preds = %104
  %85 = trunc nsw i64 %106 to i32
  %86 = trunc nsw i64 %107 to i32
  %87 = trunc nsw i64 %105 to i32
  %88 = xor i32 %87, -1
  %89 = add i32 %72, %88
  %90 = icmp sgt i32 %89, -1
  br i1 %90, label %91, label %110, !llvm.loop !15

91:                                               ; preds = %82, %84
  %92 = phi i32 [ %80, %82 ], [ %89, %84 ]
  %93 = phi i32 [ %73, %82 ], [ %87, %84 ]
  %94 = phi i32 [ %75, %82 ], [ %85, %84 ]
  %95 = phi i32 [ %76, %82 ], [ %86, %84 ]
  %96 = phi i64 [ %83, %82 ], [ %105, %84 ]
  %97 = sext i32 %95 to i64
  %98 = getelementptr inbounds i8, ptr @t, i64 %97
  %99 = load i8, ptr %98, align 1, !tbaa !9
  %100 = zext nneg i32 %92 to i64
  %101 = getelementptr inbounds nuw i8, ptr @t, i64 %100
  %102 = load i8, ptr %101, align 1, !tbaa !9
  %103 = icmp eq i8 %99, %102
  br i1 %103, label %104, label %110

104:                                              ; preds = %91
  %105 = add nsw i64 %96, 1
  %106 = add nsw i64 %105, %53
  %107 = add nsw i64 %106, 1
  %108 = icmp slt i64 %107, %39
  br i1 %108, label %84, label %109, !llvm.loop !15

109:                                              ; preds = %104
  br label %110, !llvm.loop !15

110:                                              ; preds = %84, %91, %78, %109, %71
  %111 = phi i32 [ %73, %71 ], [ %73, %78 ], [ %54, %109 ], [ %93, %91 ], [ %87, %84 ]
  %112 = phi i32 [ %75, %71 ], [ %75, %78 ], [ %40, %109 ], [ %94, %91 ], [ %85, %84 ]
  store i32 %111, ptr %74, align 4, !tbaa !5
  %113 = icmp sgt i32 %112, %56
  %114 = select i1 %113, i32 %72, i32 %57
  %115 = tail call i32 @llvm.smax.i32(i32 %112, i32 %56)
  %116 = tail call i32 @llvm.smax.i32(i32 %111, i32 %55)
  %117 = add nuw nsw i64 %53, 1
  %118 = add i32 %54, -1
  %119 = icmp eq i64 %117, %37
  br i1 %119, label %51, label %52, !llvm.loop !16
}

; Function Attrs: mustprogress nocallback nofree nounwind willreturn memory(argmem: read)
declare i64 @strlen(ptr noundef captures(none)) local_unnamed_addr #1

; Function Attrs: nofree nounwind sspstrong uwtable
define dso_local range(i32 0, 2) i32 @main() local_unnamed_addr #2 {
  %1 = tail call i32 @manacher(ptr noundef nonnull @.str)
  %2 = icmp eq i32 %1, 3
  br i1 %2, label %3, label %11

3:                                                ; preds = %0
  %4 = tail call i32 @manacher(ptr noundef nonnull @.str.2)
  %5 = icmp eq i32 %4, 2
  br i1 %5, label %6, label %11

6:                                                ; preds = %3
  %7 = tail call i32 @manacher(ptr noundef nonnull @.str.4)
  %8 = icmp ne i32 %7, 7
  %9 = select i1 %8, ptr @str.7, ptr @str
  %10 = zext i1 %8 to i32
  br label %11

11:                                               ; preds = %6, %3, %0
  %12 = phi ptr [ @str.8, %3 ], [ %9, %6 ], [ @str.9, %0 ]
  %13 = phi i32 [ 1, %3 ], [ %10, %6 ], [ 1, %0 ]
  %14 = tail call i32 @puts(ptr nonnull dereferenceable(1) %12)
  ret i32 %13
}

; Function Attrs: nofree nounwind
declare noundef i32 @puts(ptr noundef readonly captures(none)) local_unnamed_addr #3

; Function Attrs: nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none)
declare i32 @llvm.smin.i32(i32, i32) #4

; Function Attrs: nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none)
declare i32 @llvm.smax.i32(i32, i32) #4

attributes #0 = { nofree norecurse nounwind sspstrong memory(readwrite, argmem: read, inaccessiblemem: none, target_mem0: none, target_mem1: none) uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #1 = { mustprogress nocallback nofree nounwind willreturn memory(argmem: read) "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #2 = { nofree nounwind sspstrong uwtable "min-legal-vector-width"="0" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cmov,+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "tune-cpu"="generic" }
attributes #3 = { nofree nounwind }
attributes #4 = { nocallback nocreateundeforpoison nofree nosync nounwind speculatable willreturn memory(none) }
attributes #5 = { nounwind willreturn memory(read) }

!llvm.module.flags = !{!0, !1, !2, !3}
!llvm.ident = !{!4}
!llvm.errno.tbaa = !{!5}

!0 = !{i32 1, !"wchar_size", i32 4}
!1 = !{i32 8, !"PIC Level", i32 2}
!2 = !{i32 7, !"PIE Level", i32 2}
!3 = !{i32 7, !"uwtable", i32 2}
!4 = !{!"clang version 22.1.8"}
!5 = !{!6, !6, i64 0}
!6 = !{!"int", !7, i64 0}
!7 = !{!"omnipotent char", !8, i64 0}
!8 = !{!"Simple C/C++ TBAA"}
!9 = !{!7, !7, i64 0}
!10 = distinct !{!10, !11, !12, !13}
!11 = !{!"llvm.loop.mustprogress"}
!12 = !{!"llvm.loop.isvectorized", i32 1}
!13 = !{!"llvm.loop.unroll.runtime.disable"}
!14 = distinct !{!14, !11, !13, !12}
!15 = distinct !{!15, !11}
!16 = distinct !{!16, !11}
